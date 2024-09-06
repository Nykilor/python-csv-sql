from filter.organization.OrganizationFilter import OrganizationFilter
from provider.OrganizationDataProvider import OrganizationDataProvider
import streamlit

class Main:
    def __init__(self):
        self.initialize_streamlit()

    def initialize_streamlit(self):
        data_provider = OrganizationDataProvider('organizations-1000.csv')
        org_filter = OrganizationFilter(data_provider)

        streamlit.set_page_config(page_title="Organization Data", layout="wide")
        streamlit.title('Organization data')

        streamlit.sidebar.markdown("Organization data CSV")

        slider_founded = streamlit.slider('Founded after', 1970, 2024, 1970, 1)
        slider_employees = streamlit.number_input('Minimum Employees', 1, 9999)
        input_name = streamlit.text_input('Name of Organization')


        org_filter.founded_after = slider_founded
        org_filter.min_amount_of_employees = slider_employees
        org_filter.name = input_name
        data_frame = org_filter.get_organization()

        streamlit.dataframe(data_frame, hide_index=True)

main = Main()