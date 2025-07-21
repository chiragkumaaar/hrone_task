# from pydantic import BaseModel
# from typing import List

# class OrderModel(BaseModel):
#     user_id: str
#     product_ids: List[str]
from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderModel(BaseModel):
    user_id: str
    items: List[OrderItem]
