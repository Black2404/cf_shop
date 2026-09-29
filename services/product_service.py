from bson import ObjectId
from fastapi import HTTPException, status

from database import product_collection
from schemas import ProductCreate, ProductUpdate


async def get_products():
    products = []

    cursor = product_collection.find()

    async for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"],
            "image": product["image"],
            "category": product["category"],
            "is_available": product["is_available"]
        })

    return products


async def get_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product ID"
        )

    product = await product_collection.find_one({
        "_id": ObjectId(product_id)
    })

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "image": product["image"],
        "category": product["category"],
        "is_available": product["is_available"]
    }


async def create_product(product_data: ProductCreate):
    result = await product_collection.insert_one({
        "name": product_data.name,
        "price": product_data.price,
        "image": product_data.image,
        "category": product_data.category,
        "is_available": product_data.is_available
    })

    return {
        "id": str(result.inserted_id),
        "name": product_data.name,
        "price": product_data.price,
        "image": product_data.image,
        "category": product_data.category,
        "is_available": product_data.is_available
    }


async def update_product(
    product_id: str,
    product_data: ProductUpdate
):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product ID"
        )

    update_data = product_data.model_dump(
        exclude_none=True
    )

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data to update"
        )

    result = await product_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return await get_product(product_id)


async def delete_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product ID"
        )

    result = await product_collection.delete_one({
        "_id": ObjectId(product_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }