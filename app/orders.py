from fastapi import APIRouter, HTTPException
from app.schemas import OrderCreate, OrderUpdate

router = APIRouter()

# Fake in-memory DB
ORDERS_DB = {}
ORDER_ID_COUNTER = 1


@router.post("/orders")
def create_order(order: OrderCreate):
    global ORDER_ID_COUNTER

    order_data = {
        "id": ORDER_ID_COUNTER,
        "product_name": order.product_name,
        "quantity": order.quantity
    }

    ORDERS_DB[ORDER_ID_COUNTER] = order_data
    ORDER_ID_COUNTER += 1

    return order_data


@router.get("/orders/{order_id}")
def get_order(order_id: int):
    if order_id not in ORDERS_DB:
        raise HTTPException(status_code=404, detail="Order not found")

    return ORDERS_DB[order_id]


@router.put("/orders/{order_id}")
def update_order(order_id: int, order: OrderUpdate):
    if order_id not in ORDERS_DB:
        raise HTTPException(status_code=404, detail="Order not found")

    ORDERS_DB[order_id]["product_name"] = order.product_name
    ORDERS_DB[order_id]["quantity"] = order.quantity

    return ORDERS_DB[order_id]
