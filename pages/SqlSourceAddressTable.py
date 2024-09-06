
import streamlit

from filter.organization.AddressFilter import AddressFilter
from provider.AddressDataProvider import AddressDataProvider


class SqlSourceAddressTable:
    def __init__(self):
        self.initialize_streamlit()

    def initialize_streamlit(self):
        data_provider = AddressDataProvider()
        address_filter = AddressFilter(data_provider)
        streamlit.set_page_config(page_title="Address Data SQL", layout="wide")
        streamlit.title('Address Data SQL')

        input_address = streamlit.text_input('Address')
        input_address2 = streamlit.text_input('Address2')
        input_district = streamlit.text_input('District')
        input_city = streamlit.text_input('City')
        input_phone = streamlit.text_input('phone')

        address_filter.address = input_address
        address_filter.address2 = input_address2
        address_filter.district = input_district
        address_filter.city = input_city
        address_filter.phone = input_phone

        streamlit.dataframe(address_filter.get_address(), hide_index=True)

main = SqlSourceAddressTable()