TEST_ROOT_TABLES = {
    'tenders': ['/tender'],
    'awards': ['/awards'],
    'contracts': ['/contracts'],
    'planning': ['/planning'],
    'parties': ['/parties']
}
TEST_COMBINED_TABLES = {
    'documents': [
        '/planning/documents',
        '/tender/documents',
        '/awards/documents',
        '/contracts/documents',
        '/contracts/implementation/documents'
    ],
    'milestones': [
        '/planning/milestones',
        '/tender/milestones',
        '/contracts/milestones',
        '/contracts/implementation/milestones'
    ],
    'amendments': [
        "/planning/amendments",
        "/tender/amendments",
        "/awards/amendments",
        "/contracts/amendments",
        "/contracts/implementation/amendments"
    ]
}

tenders_columns = [
    '/tender/id',
    '/tender/title',
    '/tender/description',
    '/tender/status',
    '/tender/procurementMethod',
    '/tender/procurementMethodDetails',
    '/tender/procurementMethodRationale',
    '/tender/mainProcurementCategory',
    '/tender/additionalProcurementCategories',
    '/tender/awardCriteria',
    '/tender/awardCriteriaDetails',
    '/tender/submissionMethodDetails',
    '/tender/submissionMethod',

    '/tender/hasEnquiries',
    '/tender/eligibilityCriteria',
    '/tender/numberOfTenderers',
    '/tender/contractPeriod/startDate',
    '/tender/contractPeriod/endDate',
    '/tender/contractPeriod/maxExtentDate',
    '/tender/contractPeriod/durationInDays',
    '/tender/awardPeriod/startDate',
    '/tender/awardPeriod/endDate',
    '/tender/awardPeriod/maxExtentDate',
    '/tender/awardPeriod/durationInDays',
    '/tender/enquiryPeriod/startDate',
    '/tender/enquiryPeriod/endDate',
    '/tender/enquiryPeriod/maxExtentDate',
    '/tender/enquiryPeriod/durationInDays',
    '/tender/tenderPeriod/startDate',
    '/tender/tenderPeriod/endDate',
    '/tender/tenderPeriod/maxExtentDate',
    '/tender/tenderPeriod/durationInDays',
    '/tender/minValue/amount',
    '/tender/minValue/currency',
    '/tender/value/amount',
    '/tender/value/currency',
    '/tender/procuringEntity/name',
    '/tender/procuringEntity/id'
]
tenders_arrays = [
    '/tender/items',
    '/tender/tenderers',
    '/tender/items/additionalClassifications'
]
tenders_combined_columns = [
    '/tender/id',
    '/tender/title',
    '/tender/description',
    '/tender/status',
    '/tender/procurementMethod',
    '/tender/procurementMethodDetails',
    '/tender/procurementMethodRationale',
    '/tender/mainProcurementCategory',
    '/tender/additionalProcurementCategories',

    '/tender/awardCriteria',
    '/tender/awardCriteriaDetails',
    '/tender/submissionMethod',
    '/tender/submissionMethodDetails',
    '/tender/hasEnquiries',
    '/tender/eligibilityCriteria',
    '/tender/numberOfTenderers',

    '/tender/tenderers/0/name',
    '/tender/tenderers/0/id',
    '/tender/contractPeriod/startDate',
    '/tender/contractPeriod/endDate',
    '/tender/contractPeriod/maxExtentDate',
    '/tender/contractPeriod/durationInDays',
    '/tender/awardPeriod/startDate',
    '/tender/awardPeriod/endDate',
    '/tender/awardPeriod/maxExtentDate',
    '/tender/awardPeriod/durationInDays',
    '/tender/enquiryPeriod/startDate',
    '/tender/enquiryPeriod/endDate',
    '/tender/enquiryPeriod/maxExtentDate',
    '/tender/enquiryPeriod/durationInDays',
    '/tender/tenderPeriod/startDate',
    '/tender/tenderPeriod/endDate',
    '/tender/tenderPeriod/maxExtentDate',
    '/tender/tenderPeriod/durationInDays',
    '/tender/minValue/amount',
    '/tender/minValue/currency',
    '/tender/value/amount',
    '/tender/value/currency',
    '/tender/items/0/id',
    '/tender/items/0/description',
    '/tender/items/0/quantity',
    '/tender/items/0/unit/scheme',
    '/tender/items/0/unit/id',
    '/tender/items/0/unit/name',
    '/tender/items/0/unit/uri',
    '/tender/items/0/unit/value/amount',
    '/tender/items/0/unit/value/currency',
    '/tender/items/0/additionalClassifications/0/scheme',
    '/tender/items/0/additionalClassifications/0/id',
    '/tender/items/0/additionalClassifications/0/description',
    '/tender/items/0/additionalClassifications/0/uri',
    '/tender/items/0/classification/scheme',
    '/tender/items/0/classification/id',
    '/tender/items/0/classification/description',
    '/tender/items/0/classification/uri',
    '/tender/procuringEntity/name',
    '/tender/procuringEntity/id'
]

awards_columns = [
    '/awards/id',
    '/awards/title',
    '/awards/description',
    '/awards/status',
    '/awards/date',
    '/awards/contractPeriod/startDate',
    '/awards/contractPeriod/endDate',
    '/awards/contractPeriod/maxExtentDate',
    '/awards/contractPeriod/durationInDays',
    '/awards/value/amount',
    '/awards/value/currency'
]
awards_combined_columns = [
    '/awards/id',
    '/awards/title',
    '/awards/description',
    '/awards/status',
    '/awards/date',

    '/awards/contractPeriod/startDate',
    '/awards/contractPeriod/endDate',
    '/awards/contractPeriod/maxExtentDate',
    '/awards/contractPeriod/durationInDays',
    '/awards/items/0/id',
    '/awards/items/0/description',
    '/awards/items/0/quantity',
    '/awards/items/0/unit/scheme',
    '/awards/items/0/unit/id',
    '/awards/items/0/unit/name',
    '/awards/items/0/unit/uri',
    '/awards/items/0/unit/value/amount',
    '/awards/items/0/unit/value/currency',
    '/awards/items/0/additionalClassifications/0/scheme',
    '/awards/items/0/additionalClassifications/0/id',
    '/awards/items/0/additionalClassifications/0/description',
    '/awards/items/0/additionalClassifications/0/uri',
    '/awards/items/0/classification/scheme',
    '/awards/items/0/classification/id',
    '/awards/items/0/classification/description',
    '/awards/items/0/classification/uri',
    '/awards/suppliers/0/name',
    '/awards/suppliers/0/id',
    '/awards/value/amount',
    '/awards/value/currency'
]

awards_arrays = [
    '/awards/suppliers',
    '/awards/items',
    '/awards/items/additionalClassifications'
]
contracts_columns = [
    '/contracts/id',
    '/contracts/awardID',
    '/contracts/title',
    '/contracts/description',
    '/contracts/status',
    '/contracts/dateSigned',
    '/contracts/value/amount',
    '/contracts/value/currency',
    '/contracts/period/startDate',
    '/contracts/period/endDate',
    '/contracts/period/maxExtentDate',
    '/contracts/period/durationInDays'
]
contracts_arrays = [
    '/contracts/items',
    '/contracts/relatedProcesses',
    '/contracts/implementation/transactions',
    '/contracts/items/additionalClassifications'
]
contracts_combined_columns = [
    '/contracts/id',
    '/contracts/awardID',
    '/contracts/title',
    '/contracts/description',
    '/contracts/status',
    '/contracts/dateSigned',
    '/contracts/relatedProcesses/0/id',
    '/contracts/relatedProcesses/0/relationship',
    '/contracts/relatedProcesses/0/title',
    '/contracts/relatedProcesses/0/scheme',
    '/contracts/relatedProcesses/0/identifier',
    '/contracts/relatedProcesses/0/uri',

    '/contracts/implementation/transactions/0/id',
    '/contracts/implementation/transactions/0/source',
    '/contracts/implementation/transactions/0/date',
    '/contracts/implementation/transactions/0/uri',
    '/contracts/implementation/transactions/0/payee/name',
    '/contracts/implementation/transactions/0/payee/id',
    '/contracts/implementation/transactions/0/payer/name',
    '/contracts/implementation/transactions/0/payer/id',
    '/contracts/implementation/transactions/0/value/amount',
    '/contracts/implementation/transactions/0/value/currency',

    '/contracts/items/0/id',
    '/contracts/items/0/description',
    '/contracts/items/0/quantity',
    '/contracts/items/0/unit/scheme',
    '/contracts/items/0/unit/id',
    '/contracts/items/0/unit/name',
    '/contracts/items/0/unit/uri',
    '/contracts/items/0/unit/value/amount',
    '/contracts/items/0/unit/value/currency',
    '/contracts/items/0/additionalClassifications/0/scheme',
    '/contracts/items/0/additionalClassifications/0/id',
    '/contracts/items/0/additionalClassifications/0/description',
    '/contracts/items/0/additionalClassifications/0/uri',
    '/contracts/items/0/classification/scheme',
    '/contracts/items/0/classification/id',
    '/contracts/items/0/classification/description',
    '/contracts/items/0/classification/uri',
    '/contracts/value/amount',
    '/contracts/value/currency',
    '/contracts/period/startDate',
    '/contracts/period/endDate',
    '/contracts/period/maxExtentDate',
    '/contracts/period/durationInDays'
]

planning_columns = [
    '/planning/rationale',
    '/planning/budget/id',
    '/planning/budget/description',
    '/planning/budget/project',
    '/planning/budget/projectID',
    '/planning/budget/uri',
    '/planning/budget/amount/amount',
    '/planning/budget/amount/currency'
]

planning_combined_columns = [
    '/planning/rationale',
    '/planning/budget/id',
    '/planning/budget/description',
    '/planning/budget/project',
    '/planning/budget/projectID',
    '/planning/budget/uri',
    '/planning/budget/amount/amount',
    '/planning/budget/amount/currency'
]
planning_arrays = []
parties_arrays = ['/parties/additionalIdentifiers']
parties_columns = [
    '/parties/name',
    '/parties/id',
    '/parties/roles',
    '/parties/contactPoint/name',
    '/parties/contactPoint/email',
    '/parties/contactPoint/telephone',
    '/parties/contactPoint/faxNumber',
    '/parties/contactPoint/url',
    '/parties/address/streetAddress',
    '/parties/address/locality',
    '/parties/address/region',
    '/parties/address/postalCode',
    '/parties/address/countryName',
    '/parties/identifier/scheme',
    '/parties/identifier/id',
    '/parties/identifier/legalName',
    '/parties/identifier/uri'
]
parties_combined_columns = [
    '/parties/name',
    '/parties/id',
    '/parties/roles',
    '/parties/roles',
    '/parties/contactPoint/name',
    '/parties/contactPoint/email',
    '/parties/contactPoint/telephone',
    '/parties/contactPoint/faxNumber',
    '/parties/contactPoint/url',
    '/parties/address/streetAddress',
    '/parties/address/locality',
    '/parties/address/region',
    '/parties/address/postalCode',
    '/parties/address/countryName',
    '/parties/additionalIdentifiers/0/scheme',
    '/parties/additionalIdentifiers/0/id',
    '/parties/additionalIdentifiers/0/legalName',
    '/parties/additionalIdentifiers/0/uri',
    '/parties/identifier/scheme',
    '/parties/identifier/id',
    '/parties/identifier/legalName',
    '/parties/identifier/uri'
]

OCDS_TITLES_COMBINED = {
    'id': 'id',
    'ocid': 'ocid',
    'rowID': 'rowID',
    'parentID': 'parentID',
    '/amendments/amendsReleaseID': 'Amendment Amended Release (identifier)',
    '/amendments/date': 'Amendment Date',
    '/amendments/description': 'Amendment Description',
    '/amendments/id': 'Amendment Id',
    '/amendments/rationale': 'Amendment Rationale',
    '/amendments/releaseID': 'Amendment Amending Release (identifier)',

    '/awards/contractPeriod/durationInDays': 'Contract Period Duration (days)',
    '/awards/contractPeriod/endDate': 'Contract Period End Date',
    '/awards/contractPeriod/maxExtentDate': 'Contract Period Maximum Extent',
    '/awards/contractPeriod/startDate': 'Contract Period Start Date',
    '/awards/date': 'Award Date',
    '/awards/description': 'Award Description',

    '/documents/dateModified': 'Document Date Modified',
    '/documents/datePublished': 'Document Date Published',
    '/documents/description': 'Document Description',
    '/documents/documentType': 'Document Type',
    '/documents/format': 'Document Format',
    '/documents/id': 'Document Id',
    '/documents/language': 'Document Language',
    '/documents/title': 'Document Title',
    '/documents/url': 'Document Url',
    "/milestones/id": "Milestone Id",
    "/milestones/title": "Milestone Title",
    "/milestones/type": "Milestone Type",
    "/milestones/description": "Milestone Description",
    "/milestones/code": "Milestone Code",
    "/milestones/dueDate": "Milestone Due Date",
    "/milestones/dateMet": "Milestone Date Met",
    "/milestones/dateModified": "Milestone Date Modified",
    "/milestones/status": "Milestone Status",

    '/awards/id': 'Award Id',
    '/awards/items/0/additionalClassifications/0/description': 'Classification '
                                                               'Description',
    '/awards/items/0/additionalClassifications/0/id': 'Classification Id',
    '/awards/items/0/additionalClassifications/0/scheme': 'Classification Scheme',
    '/awards/items/0/additionalClassifications/0/uri': 'Classification Uri',
    '/awards/items/0/classification/description': 'Classification Description',
    '/awards/items/0/classification/id': 'Classification Id',
    '/awards/items/0/classification/scheme': 'Classification Scheme',
    '/awards/items/0/classification/uri': 'Classification Uri',
    '/awards/items/0/description': 'Item Description',
    '/awards/items/0/id': 'Item Id',
    '/awards/items/0/quantity': 'Item Quantity',
    '/awards/items/0/unit/id': 'Unit Id',
    '/awards/items/0/unit/name': 'Unit Name',
    '/awards/items/0/unit/scheme': 'Unit Scheme',
    '/awards/items/0/unit/uri': 'Unit Uri',
    '/awards/items/0/unit/value/amount': 'Value Amount',
    '/awards/items/0/unit/value/currency': 'Value Currency',
    '/awards/items/additionalClassifications/description': 'Classification '
                                                           'Description',
    '/awards/items/additionalClassifications/id': 'Classification Id',
    '/awards/items/additionalClassifications/scheme': 'Classification Scheme',
    '/awards/items/additionalClassifications/uri': 'Classification Uri',
    '/awards/items/classification/description': 'Classification Description',
    '/awards/items/classification/id': 'Classification Id',
    '/awards/items/classification/scheme': 'Classification Scheme',
    '/awards/items/classification/uri': 'Classification Uri',
    '/awards/items/description': 'Item Description',
    '/awards/items/id': 'Item Id',
    '/awards/items/quantity': 'Item Quantity',
    '/awards/items/unit/id': 'Unit Id',
    '/awards/items/unit/name': 'Unit Name',
    '/awards/items/unit/scheme': 'Unit Scheme',
    '/awards/items/unit/uri': 'Unit Uri',
    '/awards/items/unit/value/amount': 'Value Amount',
    '/awards/items/unit/value/currency': 'Value Currency',
    '/awards/status': 'Award Status',
    '/awards/suppliers/0/id': 'Organization Reference Id',
    '/awards/suppliers/0/name': 'Organization Reference Name',
    '/awards/suppliers/id': 'Organization Reference Id',
    '/awards/suppliers/name': 'Organization Reference Name',
    '/awards/title': 'Award Title',
    '/awards/value/amount': 'Value Amount',
    '/awards/value/currency': 'Value Currency',

    '/contracts/awardID': 'Contract Award Id',
    '/contracts/dateSigned': 'Contract Date Signed',
    '/contracts/description': 'Contract Description',

    '/contracts/id': 'Contract Id',

    '/contracts/implementation/transactions/0/date': 'Transaction Information '
                                                     'Date',
    '/contracts/implementation/transactions/0/id': 'Transaction Information Id',
    '/contracts/implementation/transactions/0/payee/id': 'Payee Organization Id',
    '/contracts/implementation/transactions/0/payee/name': 'Payee Organization '
                                                           'Name',
    '/contracts/implementation/transactions/0/payer/id': 'Payer Organization Id',
    '/contracts/implementation/transactions/0/payer/name': 'Payer Organization '
                                                           'Name',
    '/contracts/implementation/transactions/0/source': 'Transaction Information '
                                                       'Data Source',
    '/contracts/implementation/transactions/0/uri': 'Transaction Information '
                                                    'Linked Spending',
    '/contracts/implementation/transactions/0/value/amount': 'Value Amount',
    '/contracts/implementation/transactions/0/value/currency': 'Value Currency',
    '/contracts/implementation/transactions/date': 'Transaction Information Date',
    '/contracts/implementation/transactions/id': 'Transaction Information Id',
    '/contracts/implementation/transactions/payee/id': 'Payee Organization Id',
    '/contracts/implementation/transactions/payee/name': 'Payee Organization Name',
    '/contracts/implementation/transactions/payer/id': 'Payer Organization Id',
    '/contracts/implementation/transactions/payer/name': 'Payer Organization Name',
    '/contracts/implementation/transactions/source': 'Transaction Information '
                                                     'Data Source',
    '/contracts/implementation/transactions/uri': 'Transaction Information Linked '
                                                  'Spending',
    '/contracts/implementation/transactions/value/amount': 'Value Amount',
    '/contracts/implementation/transactions/value/currency': 'Value Currency',
    '/contracts/items/0/additionalClassifications/0/description': 'Classification '
                                                                  'Description',
    '/contracts/items/0/additionalClassifications/0/id': 'Classification Id',
    '/contracts/items/0/additionalClassifications/0/scheme': 'Classification '
                                                             'Scheme',
    '/contracts/items/0/additionalClassifications/0/uri': 'Classification Uri',
    '/contracts/items/0/classification/description': 'Classification Description',
    '/contracts/items/0/classification/id': 'Classification Id',
    '/contracts/items/0/classification/scheme': 'Classification Scheme',
    '/contracts/items/0/classification/uri': 'Classification Uri',
    '/contracts/items/0/description': 'Item Description',
    '/contracts/items/0/id': 'Item Id',
    '/contracts/items/0/quantity': 'Item Quantity',
    '/contracts/items/0/unit/id': 'Unit Id',
    '/contracts/items/0/unit/name': 'Unit Name',
    '/contracts/items/0/unit/scheme': 'Unit Scheme',
    '/contracts/items/0/unit/uri': 'Unit Uri',
    '/contracts/items/0/unit/value/amount': 'Value Amount',
    '/contracts/items/0/unit/value/currency': 'Value Currency',
    '/contracts/items/additionalClassifications/description': 'Classification '
                                                              'Description',
    '/contracts/items/additionalClassifications/id': 'Classification Id',
    '/contracts/items/additionalClassifications/scheme': 'Classification Scheme',
    '/contracts/items/additionalClassifications/uri': 'Classification Uri',
    '/contracts/items/classification/description': 'Classification Description',
    '/contracts/items/classification/id': 'Classification Id',
    '/contracts/items/classification/scheme': 'Classification Scheme',
    '/contracts/items/classification/uri': 'Classification Uri',
    '/contracts/items/description': 'Item Description',
    '/contracts/items/id': 'Item Id',
    '/contracts/items/quantity': 'Item Quantity',
    '/contracts/items/unit/id': 'Unit Id',
    '/contracts/items/unit/name': 'Unit Name',
    '/contracts/items/unit/scheme': 'Unit Scheme',
    '/contracts/items/unit/uri': 'Unit Uri',
    '/contracts/items/unit/value/amount': 'Value Amount',
    '/contracts/items/unit/value/currency': 'Value Currency',

    '/contracts/period/durationInDays': 'Period Duration (days)',
    '/contracts/period/endDate': 'Period End Date',
    '/contracts/period/maxExtentDate': 'Period Maximum Extent',
    '/contracts/period/startDate': 'Period Start Date',
    '/contracts/relatedProcesses/0/id': 'Related Process Relationship Id',
    '/contracts/relatedProcesses/0/identifier': 'Related Process Identifier',
    '/contracts/relatedProcesses/0/relationship': 'Related Process Relationship',
    '/contracts/relatedProcesses/0/scheme': 'Related Process Scheme',
    '/contracts/relatedProcesses/0/title': 'Related Process Title',
    '/contracts/relatedProcesses/0/uri': 'Related Process Uri',
    '/contracts/relatedProcesses/id': 'Related Process Relationship Id',
    '/contracts/relatedProcesses/identifier': 'Related Process Identifier',
    '/contracts/relatedProcesses/relationship': 'Related Process Relationship',
    '/contracts/relatedProcesses/scheme': 'Related Process Scheme',
    '/contracts/relatedProcesses/title': 'Related Process Title',
    '/contracts/relatedProcesses/uri': 'Related Process Uri',
    '/contracts/status': 'Contract Status',
    '/contracts/title': 'Contract Title',
    '/contracts/value/amount': 'Value Amount',
    '/contracts/value/currency': 'Value Currency',
    '/ocid': 'Open Contracting Id',
    '/parties/additionalIdentifiers/0/id': 'Identifier Id',
    '/parties/additionalIdentifiers/0/legalName': 'Identifier Legal Name',
    '/parties/additionalIdentifiers/0/scheme': 'Identifier Scheme',
    '/parties/additionalIdentifiers/0/uri': 'Identifier Uri',
    '/parties/additionalIdentifiers/id': 'Identifier Id',
    '/parties/additionalIdentifiers/legalName': 'Identifier Legal Name',
    '/parties/additionalIdentifiers/scheme': 'Identifier Scheme',
    '/parties/additionalIdentifiers/uri': 'Identifier Uri',
    '/parties/address/countryName': 'Address Country Name',
    '/parties/address/locality': 'Address Locality',
    '/parties/address/postalCode': 'Address Postal Code',
    '/parties/address/region': 'Address Region',
    '/parties/address/streetAddress': 'Address Street',
    '/parties/contactPoint/email': 'Contact Point Email',
    '/parties/contactPoint/faxNumber': 'Contact Point Fax Number',
    '/parties/contactPoint/name': 'Contact Point Name',
    '/parties/contactPoint/telephone': 'Contact Point Telephone',
    '/parties/contactPoint/url': 'Contact Point Url',
    '/parties/id': 'Organization Entity Id',
    '/parties/identifier/id': 'Primary Identifier Id',
    '/parties/identifier/legalName': 'Primary Identifier Legal Name',
    '/parties/identifier/scheme': 'Primary Identifier Scheme',
    '/parties/identifier/uri': 'Primary Identifier Uri',
    '/parties/name': 'Organization Common Name',
    '/parties/roles': 'Organization Party Roles',
    '/parties/roles/0': 'Organization Party Roles',
    '/planning/budget/amount/amount': 'Amount',
    '/planning/budget/amount/currency': 'Amount Currency',
    '/planning/budget/description': 'Budget Source',
    '/planning/budget/id': 'Budget Id',
    '/planning/budget/project': 'Budget Project Title',
    '/planning/budget/projectID': 'Budget Project Identifier',
    '/planning/budget/uri': 'Budget Linked Information',

    '/planning/rationale': 'Planning Rationale',
    '/tender/additionalProcurementCategories': 'Tender Additional Procurement '
                                               'Categories',
    '/tender/additionalProcurementCategories/0': 'Tender Additional Procurement '
                                                 'Categories',
    '/tender/amendments/0/amendsReleaseID': 'Amendment Amended Release '
                                            '(identifier)',

    '/tender/awardCriteria': 'Tender Award Criteria',
    '/tender/awardCriteriaDetails': 'Tender Award Criteria Details',
    '/tender/awardPeriod/durationInDays': 'Evaluation And Award Period Duration '
                                          '(days)',
    '/tender/awardPeriod/endDate': 'Evaluation And Award Period End Date',
    '/tender/awardPeriod/maxExtentDate': 'Evaluation And Award Period Maximum '
                                         'Extent',
    '/tender/awardPeriod/startDate': 'Evaluation And Award Period Start Date',
    '/tender/contractPeriod/durationInDays': 'Contract Period Duration (days)',
    '/tender/contractPeriod/endDate': 'Contract Period End Date',
    '/tender/contractPeriod/maxExtentDate': 'Contract Period Maximum Extent',
    '/tender/contractPeriod/startDate': 'Contract Period Start Date',
    '/tender/description': 'Tender Description',

    '/tender/eligibilityCriteria': 'Tender Eligibility Criteria',
    '/tender/enquiryPeriod/durationInDays': 'Enquiry Period Duration (days)',
    '/tender/enquiryPeriod/endDate': 'Enquiry Period End Date',
    '/tender/enquiryPeriod/maxExtentDate': 'Enquiry Period Maximum Extent',
    '/tender/enquiryPeriod/startDate': 'Enquiry Period Start Date',
    '/tender/hasEnquiries': 'Tender Has Enquiries?',
    '/tender/id': 'Tender Id',
    '/tender/items/0/additionalClassifications/0/description': 'Classification '
                                                               'Description',
    '/tender/items/0/additionalClassifications/0/id': 'Classification Id',
    '/tender/items/0/additionalClassifications/0/scheme': 'Classification Scheme',
    '/tender/items/0/additionalClassifications/0/uri': 'Classification Uri',
    '/tender/items/0/classification/description': 'Classification Description',
    '/tender/items/0/classification/id': 'Classification Id',
    '/tender/items/0/classification/scheme': 'Classification Scheme',
    '/tender/items/0/classification/uri': 'Classification Uri',
    '/tender/items/0/description': 'Item Description',
    '/tender/items/0/id': 'Item Id',
    '/tender/items/0/quantity': 'Item Quantity',
    '/tender/items/0/unit/id': 'Unit Id',
    '/tender/items/0/unit/name': 'Unit Name',
    '/tender/items/0/unit/scheme': 'Unit Scheme',
    '/tender/items/0/unit/uri': 'Unit Uri',
    '/tender/items/0/unit/value/amount': 'Value Amount',
    '/tender/items/0/unit/value/currency': 'Value Currency',
    '/tender/items/additionalClassifications/description': 'Classification '
                                                           'Description',
    '/tender/items/additionalClassifications/id': 'Classification Id',
    '/tender/items/additionalClassifications/scheme': 'Classification Scheme',
    '/tender/items/additionalClassifications/uri': 'Classification Uri',
    '/tender/items/classification/description': 'Classification Description',
    '/tender/items/classification/id': 'Classification Id',
    '/tender/items/classification/scheme': 'Classification Scheme',
    '/tender/items/classification/uri': 'Classification Uri',
    '/tender/items/description': 'Item Description',
    '/tender/items/id': 'Item Id',
    '/tender/items/quantity': 'Item Quantity',
    '/tender/items/unit/id': 'Unit Id',
    '/tender/items/unit/name': 'Unit Name',
    '/tender/items/unit/scheme': 'Unit Scheme',
    '/tender/items/unit/uri': 'Unit Uri',
    '/tender/items/unit/value/amount': 'Value Amount',
    '/tender/items/unit/value/currency': 'Value Currency',
    '/tender/mainProcurementCategory': 'Tender Main Procurement Category',

    '/tender/minValue/amount': 'Minimum Value Amount',
    '/tender/minValue/currency': 'Minimum Value Currency',
    '/tender/numberOfTenderers': 'Tender Number Of Tenderers',
    '/tender/procurementMethod': 'Tender Procurement Method',
    '/tender/procurementMethodDetails': 'Tender Procurement Method Details',
    '/tender/procurementMethodRationale': 'Tender Procurement Method Rationale',
    '/tender/procuringEntity/id': 'Procuring Entity Organization Id',
    '/tender/procuringEntity/name': 'Procuring Entity Organization Name',
    '/tender/status': 'Tender Status',
    '/tender/submissionMethod': 'Tender Submission Method',
    '/tender/submissionMethod/0': 'Tender Submission Method',
    '/tender/submissionMethodDetails': 'Tender Submission Method Details',
    '/tender/tenderPeriod/durationInDays': 'Tender Period Duration (days)',
    '/tender/tenderPeriod/endDate': 'Tender Period End Date',
    '/tender/tenderPeriod/maxExtentDate': 'Tender Period Maximum Extent',
    '/tender/tenderPeriod/startDate': 'Tender Period Start Date',
    '/tender/tenderers/0/id': 'Organization Reference Id',
    '/tender/tenderers/0/name': 'Organization Reference Name',
    '/tender/tenderers/id': 'Organization Reference Id',
    '/tender/tenderers/name': 'Organization Reference Name',
    '/tender/title': 'Tender Title',
    '/tender/value/amount': 'Value Amount',
    '/tender/value/currency': 'Value Currency'

}
