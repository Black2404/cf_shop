from fastapi import HTTPException, status

from database import user_collection
from schemas import StaffCreate
from utils.security import hash_password
from bson import ObjectId

# Add staff
async def create_staff(staff_data: StaffCreate):
    existing_staff = await user_collection.find_one({
        "username": staff_data.username
    })

    if existing_staff:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_password = hash_password(staff_data.password)

    result = await user_collection.insert_one({
        "username": staff_data.username,
        "password": hashed_password,
        "role": "staff"
    })

    return {
        "id": str(result.inserted_id),
        "username": staff_data.username,
        "role": "staff"
    }

# List staff
async def get_staffs():
    staffs = []

    cursor = user_collection.find({
        "role": "staff"
    })

    async for staff in cursor:
        staffs.append({
            "id": str(staff["_id"]),
            "username": staff["username"],
            "role": staff["role"]
        })

    return staffs

# Delete staff
async def delete_staff(staff_id: str):
    if not ObjectId.is_valid(staff_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid staff ID"
        )

    result = await user_collection.delete_one({
        "_id": ObjectId(staff_id),
        "role": "staff"
    })

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found"
        )

    return {
        "message": "Staff deleted successfully"
    }