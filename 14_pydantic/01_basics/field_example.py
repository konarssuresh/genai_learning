from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities : Dict[str, int]

class Blog(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    'user_id':123,
    'items': ['laptop','mouse','keyboard'],
    'quantities': {
        'laptop':1,
        'keyboard':2,
        'mouse': 3
    }
}

cart = Cart(**cart_data)
print(cart)