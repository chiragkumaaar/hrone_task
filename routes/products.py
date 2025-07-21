from fastapi import APIRouter, Query
from models.product import ProductModel
from database import products_collection

router = APIRouter()

@router.post("/products", status_code=201)
def create_product(product: ProductModel):
    result = products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products")
def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes"] = size

    products = products_collection.find(query).skip(offset).limit(limit)

    return [
        {
            "_id": str(prod["_id"]),
            "name": prod["name"],
            "description": prod.get("description"),
            "price": prod["price"],
            "sizes": prod["sizes"]
        }
        for prod in products
    ]
