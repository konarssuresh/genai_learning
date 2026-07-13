from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at:datetime 
    address: Address
    tags: List[str]=[]

    model_config = ConfigDict(
        json_encoders={datetime: lambda v:v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Suresh",
    email='suresh@gmail.com',
    created_at=datetime(2024,3,15,14,30),
    address=Address(
        street='something',
        city='some city',
        postal_code='123123'
    ),
    is_active=False,
    tags=['premium','subscriber']
)


dict_py = user.model_dump()
print(user.model_dump())
print(user)


json_str = user.model_dump_json()
print("="*300)
print(json_str)