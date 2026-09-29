from database import order_collection


async def get_revenue():
    pipeline = [
        {
            "$match": {
                "payment_status": "paid"
            }
        },
        {
            "$group": {
                "_id": None,
                "total_revenue": {"$sum": "$total"}
            }
        }
    ]

    result = await order_collection.aggregate(pipeline).to_list(length=1)

    if not result:
        return {
            "total_revenue": 0
        }

    return {
        "total_revenue": result[0]["total_revenue"]
    }