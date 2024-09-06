import pandas


class OrganizationDataProvider:
    COLUMN_INDEX = 'Index'
    COLUMN_ORGANIZATION_ID = 'Organization Id'
    COLUMN_NAME = 'Name'
    COLUMN_WEBSITE = 'Website'
    COLUMN_COUNTRY = 'Country'
    COLUMN_DESCRIPTION = 'Description'
    COLUMN_FOUNDED = 'Founded'
    COLUMN_INDUSTRY = 'Industry'
    COLUMN_NUMBER_OF_EMPLOYEES = 'Number of employees'

    def __init__(
            self,
            organization_file_path: str
    ):
        self.organization_data = pandas.read_csv(organization_file_path)
