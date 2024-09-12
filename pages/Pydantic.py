import json
from json import detect_encoding

import streamlit
from charset_normalizer import from_bytes
from numpy.random import geometric
from pandas.api.types import infer_dtype

from model.AddressModel import AddressModel
from provider.AddressDataProvider import AddressDataProvider


class Pydantic:
    def __init__(self):
        self.initialize_streamlit()

    def initialize_streamlit(self):
        data_provider = AddressDataProvider()
        streamlit.set_page_config(page_title="Pydantic Address JSON by ID")
        streamlit.title('Pydantic Address JSON by ID')

        input_id = streamlit.text_input('ID', value=1)
        data_frame = data_provider.address_data

        address_data = data_frame.loc[data_frame[data_provider.COLUMN_ID] == int(input_id)]

        if not address_data.empty:
            address_model = AddressModel(**address_data.iloc[0].to_dict())
            streamlit.write('Raw Model:')
            streamlit.write(address_model)
            streamlit.write('Json Serialized Model:')
            streamlit.write(address_model.model_dump_json())
        else:
            streamlit.write("Empty nothing found")


main = Pydantic()