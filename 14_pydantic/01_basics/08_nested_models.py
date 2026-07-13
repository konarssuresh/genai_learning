from typing import List,Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street='123 something',
    city='Pune',
    postal_code='100202'
)

user = User(
    id=1,
    name='Suresh',
    address=address
)

user_data = {
    'id':1,
    'name':"Suresh",
    'address':{
        'street':'123 something',
        'city':'pune',
        'postal_code':'122222'
    }
}


user2 = User(**user_data)

print(user2)