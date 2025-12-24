from fastapi import FastAPI
from app.orders import router as orders_router

app = FastAPI(title="Order Service")

app.include_router(orders_router)
