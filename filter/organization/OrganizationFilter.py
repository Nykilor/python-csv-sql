from altair import condition

from provider.OrganizationDataProvider import OrganizationDataProvider
import pandas


class OrganizationFilter:
    name : str = ''
    founded_after : int = 1970
    min_amount_of_employees : int = 1

    def __init__(self, organization_data: OrganizationDataProvider):
        self.organization_data = organization_data
        self.data_frame = organization_data.organization_data

    def get_organization(self) -> pandas.DataFrame:
        org = self.organization_data
        df = self.data_frame

        conditions = (df[org.COLUMN_NUMBER_OF_EMPLOYEES] > self.min_amount_of_employees) & (df[org.COLUMN_FOUNDED] > self.founded_after)

        if self.name:
            conditions = conditions & (df[org.COLUMN_NAME].str.contains(self.name))

        return df.loc[conditions]
