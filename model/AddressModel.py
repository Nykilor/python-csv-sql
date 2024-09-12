import json
from typing import Optional, Annotated

from charset_normalizer import from_bytes
from pydantic import BaseModel, PlainSerializer
from pyodbc import Timestamp

CustomTimeStamp = Annotated[
    Timestamp, PlainSerializer(lambda x: x.isoformat(), return_type=str)
]

LocationType = Annotated[
    Optional[bytes], PlainSerializer(lambda x: str(x), return_type=str)
]

class AddressModel(BaseModel):
    address_id: int
    address: Optional[str] = None
    address2: Optional[str] = None
    district: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    location: LocationType
    last_update: CustomTimeStamp
