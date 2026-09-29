from fastapi import FastAPI

from routers.auth import router as auth_router
from routers.staff import router as staff_router
from routers.products import router as product_router
from routers.tables import router as table_router
from routers.orders import router as order_router
from routers.revenue import router as revenue_router


app = FastAPI(title="Cafe Shop API")

app.include_router(auth_router)
app.include_router(staff_router)
app.include_router(product_router)
app.include_router(table_router)
app.include_router(order_router)
app.include_router(revenue_router)
