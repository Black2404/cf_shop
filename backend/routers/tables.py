from fastapi import APIRouter, Depends

from schemas import TableResponse, TableUpdate
from services.table_service import get_tables, update_table
from utils.dependencies import get_current_user

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.get("", response_model=list[TableResponse])
async def get_all_tables(
    current_user: dict = Depends(get_current_user)
):
    return await get_tables()


@router.put("/{table_number}", response_model=TableResponse)
async def update_table_status(
    table_number: int,
    table_data: TableUpdate,
    current_user: dict = Depends(get_current_user)
):
    return await update_table(table_number, table_data)