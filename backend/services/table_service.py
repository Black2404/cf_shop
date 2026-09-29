from fastapi import HTTPException, status

from database import table_collection
from schemas import TableUpdate


async def get_tables():
    tables = []

    cursor = table_collection.find().sort("table_number", 1)

    async for table in cursor:
        tables.append({
            "table_number": table["table_number"],
            "status": table["status"]
        })

    return tables


async def update_table(
    table_number: int,
    table_data: TableUpdate
):
    result = await table_collection.update_one(
        {
            "table_number": table_number
        },
        {
            "$set": {
                "status": table_data.status
            }
        }
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Table not found"
        )

    return {
        "table_number": table_number,
        "status": table_data.status
    }