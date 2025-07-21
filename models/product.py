from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    name: str
    description: Optional[str]
    price: float
    sizes: List[str]
