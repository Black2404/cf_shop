from pydantic import BaseModel, Field
from typing import Literal

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=100)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    username: str
    role: str

class StaffCreate(LoginRequest):
    pass

class StaffResponse(BaseModel):
    id: str
    username: str
    role: str

class DeleteStaffResponse(BaseModel):
    message: str

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    image: str
    category: str
    is_available: bool = True


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    price: float | None = Field(None, gt=0)
    image: str | None = None
    category: str | None = None
    is_available: bool | None = None


class ProductResponse(ProductCreate):
    id: str
    is_available: bool

class DeleteProductResponse(BaseModel):
    message: str

class TableResponse(BaseModel):
    table_number: int
    status: Literal["available", "occupied"]


class TableUpdate(BaseModel):
    status: Literal["available", "occupied"]

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]
    order_type: Literal["take_away", "dine_in"]
    table_number: int | None = None


class OrderItemResponse(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int
    subtotal: float


class OrderResponse(OrderCreate):
    id: str
    total: float
    payment_status: Literal["unpaid", "paid"]

class PaymentResponse(BaseModel):
    message: str
    order_id: str
    payment_status: Literal["paid"]

class RevenueResponse(BaseModel):
    total_revenue: float