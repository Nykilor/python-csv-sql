from altair import condition

from provider.AddressDataProvider import AddressDataProvider
from provider.OrganizationDataProvider import OrganizationDataProvider
import pandas


class AddressFilter:
    address: str = ''
    address2: str = ''
    district: str = ''
    city: str = ''
    postal_code: str = ''
    phone: str = ''

    def __init__(self, address_data: AddressDataProvider):
        self.provider = address_data
        self.address_data = address_data.address_data

    def get_address(self) -> pandas.DataFrame:
        provider = self.provider
        df = self.address_data

        conditions = (df[provider.COLUMN_ID] > 0)

        if self.address:
            conditions = conditions & (df[provider.COLUMN_ADDRESS].str.contains(self.address))

        if self.address2:
            conditions = conditions & (df[provider.COLUMN_ADDRESS2].str.contains(self.address2))

        if self.district:
            conditions = conditions & (df[provider.COLUMN_DISTRICT].str.contains(self.district))

        if self.city:
            conditions = conditions & (df[provider.COLUMN_CITY].str.contains(self.city))

        if self.phone:
            conditions = conditions & (df[provider.COLUMN_PHONE].str.contains(self.phone))

        return df.loc[conditions]