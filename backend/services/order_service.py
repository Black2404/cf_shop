from bson import ObjectId
from fastapi import HTTPException, status

from database import order_collection, product_collection, table_collection
from schemas import OrderCreate


async def create_order(order_data: OrderCreate):
    # 1. Kiểm tra loại order
    if order_data.order_type == "dine_in":
        if order_data.table_number is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Table number is required"
            )

        table = await table_collection.find_one({
            "table_number": order_data.table_number
        })

        if not table:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Table not found"
            )

        if table["status"] == "occupied":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Table is occupied"
            )

    # 2. Lấy thông tin sản phẩm và tính tiền
    items = []
    total = 0

    for item in order_data.items:
        if not ObjectId.is_valid(item.product_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid product ID"
            )

        product = await product_collection.find_one({
            "_id": ObjectId(item.product_id)
        })

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        subtotal = product["price"] * item.quantity
        total += subtotal

        items.append({
            "product_id": item.product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    # 3. Tạo order
    order = {
        "items": items,
        "order_type": order_data.order_type,
        "table_number": order_data.table_number,
        "total": total,
        "payment_status": "unpaid"
    }

    result = await order_collection.insert_one(order)

    # 4. Nếu dine-in thì chuyển bàn thành occupied
    if order_data.order_type == "dine_in":
        await table_collection.update_one(
            {"table_number": order_data.table_number},
            {"$set": {"status": "occupied"}}
        )

    return {
        "id": str(result.inserted_id),
        **order
    }

async def pay_order(order_id: str):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order ID"
        )

    result = await order_collection.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"payment_status": "paid"}}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    return {
        "message": "Payment successful",
        "order_id": order_id,
        "payment_status": "paid"
    }