from fastapi import APIRouter
from models.order import OrderModel
from database import orders_collection

router = APIRouter()

@router.post("/orders", status_code=201)
def create_order(order: OrderModel):
    result = orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    return [
        {
            "_id": str(order["_id"]),
            "user_id": order["user_id"],
            "items": order["items"]  # ✅ changed from product_ids
        }
        for order in orders
    ]

# from fastapi import APIRouter, HTTPException
# from models.order import OrderModel, OrderDBModel
# from config.database import order_collection
# from bson import ObjectId

# router = APIRouter()

# @router.post("/orders", response_model=dict, status_code=201)
# async def create_order(order: OrderModel):
#     # Convert to dict and insert
#     order_dict = order.dict()
#     result = await order_collection.insert_one(order_dict)
#     return {"id": str(result.inserted_id)}

# @router.get("/orders", response_model=list[OrderDBModel])
# async def list_orders():
#     orders = []
#     async for order in order_collection.find():
#         order["id"] = str(order["_id"])
#         orders.append(OrderDBModel(**order))
#     return orders

