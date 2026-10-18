from fastapi import APIRouter, Depends

from schemas import OrderCreate, PaymentResponse
from services.order_service import create_order
from utils.dependencies import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("", response_model=PaymentResponse)
async def create_new_order(
    order_data: OrderCreate,
    current_user: dict = Depends(get_current_user)
):
    return await create_order(order_data)
