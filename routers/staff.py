from fastapi import APIRouter, Depends

from utils.dependencies import require_admin
from schemas import (
    StaffCreate,
    StaffResponse,
    DeleteStaffResponse
)

from services.staff_service import (
    create_staff,
    get_staffs,
    delete_staff
)

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

# Add staff
@router.post("", response_model=StaffResponse)
async def create_staff_account(
    staff_data: StaffCreate,
    current_user: dict = Depends(require_admin)
):
    return await create_staff(staff_data)

# List staff
@router.get("", response_model=list[StaffResponse])
async def get_staff_accounts(
    current_user: dict = Depends(require_admin)
):
    return await get_staffs()

# Delete staff
@router.delete("/{staff_id}", response_model=DeleteStaffResponse)
async def delete_staff_account(
    staff_id: str,
    current_user: dict = Depends(require_admin)
):
    return await delete_staff(staff_id)