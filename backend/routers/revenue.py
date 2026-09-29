from fastapi import APIRouter, Depends

from schemas import RevenueResponse
from services.revenue_service import get_revenue
from utils.dependencies import require_admin


router = APIRouter(
    prefix="/revenue",
    tags=["Revenue"]
)


@router.get("", response_model=RevenueResponse)
async def get_total_revenue(
    current_user: dict = Depends(require_admin)
):
    return await get_revenue()