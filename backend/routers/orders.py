from fastapi import APIRouter, Depends

from schemas import OrderCreate, OrderResponse
from services.order_service import create_order
from utils.dependencies import get_current_user
from schemas import OrderCreate, OrderResponse, PaymentResponse
from services.order_service import create_order, pay_order


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("", response_model=OrderResponse)
async def create_new_order(
    order_data: OrderCreate,
    current_user: dict = Depends(get_current_user)
):
    return await create_order(order_data)

@router.put("/{order_id}/pay", response_model=PaymentResponse)
async def pay_existing_order(
    order_id: str,
    current_user: dict = Depends(get_current_user)
):
    return await pay_order(order_id)
