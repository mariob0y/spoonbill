from pathlib import Path
from unittest.mock import call, patch

from spoonbill import FileFlattener
from spoonbill.flatten import Flattener, FlattenOptions

from .conftest import releases_path
from .utils import get_writers, prepare_tables, read_csv_headers, read_xlsx_headers

ID_FIELDS = {"tenders": "/tender/id", "parties": "/parties/id"}


def test_writer_init(spec, tmpdir, flatten_options):
    tables = prepare_tables(spec, flatten_options, ID_FIELDS)
    workdir = Path(tmpdir)
    get_writers(workdir, tables, flatten_options)
    path = workdir / "result.xlsx"

    assert path.is_file()
    for name in flatten_options.selection:
        path = workdir / f"{name}.csv"
        assert path.is_file()


def test_headers_filtering(spec, tmpdir, flatten_options):
    tables = prepare_tables(spec, flatten_options, ID_FIELDS)
    workdir = Path(tmpdir)
    get_writers(workdir, tables, flatten_options)
    for name in flatten_options.selection:
        path = workdir / f"{name}.csv"
        xlsx_headers = read_xlsx_headers(workdir / "result.xlsx", name)
        csv_headers = read_csv_headers(path)
        assert len(xlsx_headers) == 1
        assert len(csv_headers) == 1
        assert xlsx_headers[0] == ID_FIELDS[name]
        assert csv_headers[0] == ID_FIELDS[name]


def test_writers_pretty_headers(spec, tmpdir, releases):
    # increase items count for force split
    releases[0]["tender"]["items"] = releases[0]["tender"]["items"] * 6
    for _ in spec.process_items(releases):
        pass
    options = FlattenOptions(
        **{
            "selection": {
                "tenders": {"split": True, "pretty_headers": True},
                "parties": {"split": False, "pretty_headers": True},
                "tenders_items": {
                    "split": True,
                    "headers": {"/tender/items/id": "item id"},
                    "pretty_headers": True,
                },
            }
        }
    )
    tables = {
        "tenders": spec.tables["tenders"],
        "parties": spec.tables["parties"],
        "tenders_items": spec.tables["tenders_items"],
    }

    workdir = Path(tmpdir)
    get_writers(workdir, tables, options)
    xlsx = workdir / "result.xlsx"

    for name, opts in options.selection.items():
        path = workdir / f"{name}.csv"
        xlsx_headers = read_xlsx_headers(xlsx, name)
        csv_headers = read_csv_headers(path)
        table = tables[name]
        for col in tables[name].available_rows(opts.split):
            title = table.titles.get(col)
            if col == "/tender/items/id":
                title = "item id"
            assert title in xlsx_headers
            assert title in csv_headers

    options = FlattenOptions(
        **{
            "selection": {
                "tenders": {
                    "split": True,
                    "headers": {"/tender/id": "TENDER"},
                    "pretty_headers": True,
                },
                "tenders_items": {
                    "split": True,
                    "headers": {"/tender/items/id": "item id"},
                    "pretty_headers": True,
                },
                "parties": {
                    "split": False,
                    "headers": {"/parties/id": "PARTY"},
                    "pretty_headers": True,
                },
            }
        }
    )

    workdir = Path(tmpdir)
    get_writers(workdir, tables, options)
    xlsx = workdir / "result.xlsx"

    sheet = "tenders"
    path = workdir / f"{sheet}.csv"
    xlsx_headers = read_xlsx_headers(xlsx, sheet)
    csv_headers = read_csv_headers(path)
    assert "TENDER" in xlsx_headers
    assert "TENDER" in csv_headers

    sheet = "tenders_items"
    path = workdir / f"{sheet}.csv"
    xlsx_headers = read_xlsx_headers(xlsx, sheet)
    csv_headers = read_csv_headers(path)
    assert "item id" in xlsx_headers
    assert "item id" in csv_headers

    xlsx = workdir / "result.xlsx"
    sheet = "parties"
    path = workdir / f"{sheet}.csv"

    xlsx_headers = read_xlsx_headers(xlsx, sheet)
    csv_headers = read_csv_headers(path)

    assert "PARTY" in xlsx_headers
    assert "PARTY" in csv_headers


def test_writers_flatten_count(spec, tmpdir, releases):
    releases[0]["tender"]["items"] = releases[0]["tender"]["items"] * 6
    for _ in spec.process_items(releases):
        pass
    options = FlattenOptions(
        **{
            "selection": {
                "tenders": {"split": True, "pretty_headers": True},
                "parties": {"split": True, "pretty_headers": True},
                "tenders_items": {
                    "split": False,
                    "pretty_headers": True,
                },
            },
            "count": True,
        }
    )

    workdir = Path(tmpdir)
    flattener = FileFlattener(workdir, options, spec.tables, root_key="releases", csv=True, xlsx=True)
    xlsx = workdir / "result.xlsx"
    for _ in flattener.flatten_file(releases_path):
        pass
    sheet = "tenders"
    path = workdir / f"{sheet}.csv"
    for headers in read_xlsx_headers(xlsx, sheet), read_csv_headers(path):
        assert "Items Count" in headers
        assert "Tenderers Count" in headers

    sheet = "parties"
    path = workdir / f"{sheet}.csv"
    for headers in read_xlsx_headers(xlsx, sheet), read_csv_headers(path):
        assert "Additional Identifiers Count" in headers


def test_writers_table_name_override(spec, tmpdir):
    options = FlattenOptions(
        **{
            "selection": {
                "parties": {"split": False, "pretty_headers": True, "name": "testname"},
                "tenders": {"split": True, "pretty_headers": True, "name": "my_tenders"},
                "tenders_items": {"split": False, "pretty_headers": True, "name": "pretty_items"},
            }
        }
    )
    tables = prepare_tables(spec, options)
    for name, table in tables.items():
        for col in table:
            table.inc_column(col, col)

    workdir = Path(tmpdir)
    get_writers(workdir, tables, options)
    xlsx = workdir / "result.xlsx"
    for name in ("testname", "my_tenders", "pretty_items"):
        path = workdir / f"{name}.csv"
        assert path.is_file()
        assert read_xlsx_headers(xlsx, name)
        assert read_csv_headers(path)


def test_abbreviations(spec, tmpdir):
    options = FlattenOptions(
        **{
            "selection": {
                "tenders_items_class": {"split": False},
                "parties_ids": {"split": False},
                "transactions": {"split": False},
            }
        }
    )
    new_names = ["tenders_items_class", "parties_ids", "transactions"]
    tables = prepare_tables(spec, options)
    for name, table in tables.items():
        for col in table:
            table.inc_column(col, col)

    workdir = Path(tmpdir)
    get_writers(workdir, tables, options)
    xlsx = workdir / "result.xlsx"
    for name in new_names:
        path = workdir / f"{name}.csv"
        assert path.is_file()
        assert read_xlsx_headers(xlsx, name)
        assert read_csv_headers(path)

def test_name_duplicate(spec, tmpdir):
    duplicate_name = "test"
    options = FlattenOptions(
        **{
            "selection": {
                "parties": {"split": False, "pretty_headers": True, "name": duplicate_name},
                "tenders": {"split": True, "pretty_headers": True, "name": duplicate_name},
                "tenders_items": {"split": False, "pretty_headers": True, "name": duplicate_name},
            }
        }
    )
    tables = prepare_tables(spec, options)
    for name, table in tables.items():
        for col in table:
            table.inc_column(col)
    workdir = Path(tmpdir)
    get_writers(workdir, tables, options)
    xlsx = workdir / "result.xlsx"
    for name in ("test", "test1", "test2"):
        path = workdir / f"{name}.csv"
        assert path.is_file()
        assert read_xlsx_headers(xlsx, name)
        assert read_csv_headers(path)


@patch("spoonbill.LOGGER.error")
def test_writers_invalid_table(log, spec, tmpdir):
    options = FlattenOptions(
        **{
            "selection": {
                "parties": {"split": False, "pretty_headers": True, "name": "testname"},
            }
        }
    )
    tables = prepare_tables(spec, options)
    for name, table in tables.items():
        for col in table:
            table.inc_column(col, col)

    workdir = Path(tmpdir)
    writers = get_writers(workdir, tables, options)
    for writer in writers:
        writer.writerow("test", {})
    log.assert_has_calls([call("Invalid table test"), call("Invalid table test")])


@patch("spoonbill.LOGGER.error")
def test_writers_invalid_row(log, spec, tmpdir):
    options = FlattenOptions(
        **{
            "selection": {
                "parties": {"split": False, "pretty_headers": True, "name": "testname"},
            }
        }
    )
    tables = prepare_tables(spec, options)
    for name, table in tables.items():
        for col in table:
            table.inc_column(col, col)

    workdir = Path(tmpdir)
    writers = get_writers(workdir, tables, options)
    for writer in writers:
        writer.writerow("parties", {"/test/test": "test"})
    log.assert_has_calls(
        [
            call("Operation produced invalid path. This a software bug, please send issue to developers"),
            call("Failed to write row None with error dict contains fields not in fieldnames: '/test/test'"),
            call("Operation produced invalid path. This a software bug, please send issue to developers"),
            call("Failed to write column /test/test to xlsx sheet parties"),
        ]
    )