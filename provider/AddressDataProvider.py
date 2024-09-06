import pandas
import sqlalchemy


class AddressDataProvider:
    COLUMN_ID = 'address_id'
    COLUMN_ADDRESS = 'address'
    COLUMN_ADDRESS2 = 'address2'
    COLUMN_DISTRICT = 'district'
    COLUMN_CITY = 'city'
    COLUMN_POSTAL_CODE = 'postal_code'
    COLUMN_PHONE = 'phone'
    COLUMN_LOCATION = 'location'
    COLUMN_LAST_UPDATE = 'last_update'

    def __init__(
            self
    ):
        engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/sakila', echo=False)
        data = pandas.read_sql(
            'SELECT address_id, address, address2, district, city.city as city,postal_code,phone,location,address.last_update as last_update FROM address LEFT JOIN city ON address.city_id = city.city_id',
            engine)
        self.address_data = data
