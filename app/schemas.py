from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_name: str
    quantity: int

class OrderUpdate(BaseModel):
    product_name: str
    quantity: int

'''class OrderResponse(BaseModel):
    id: int
    product_name: str
    quantity: int
    user_email: str

    class Config:
        from_attributes = True'''







