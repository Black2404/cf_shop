from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from routers.auth import router as auth_router
from routers.staff import router as staff_router
from routers.products import router as product_router
from routers.tables import router as table_router
from routers.orders import router as order_router
from routers.revenue import router as revenue_router


app = FastAPI(title="Cafe Shop API")

# Configure CORS to allow the Frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200",],  # Allow all websites to access the API
    allow_credentials=True, # Allow sending cookies or authentication information
    allow_methods=["*"], # Allow sending all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Allow sending all Headers
)

app.include_router(auth_router)
app.include_router(staff_router)
app.include_router(product_router)
app.include_router(table_router)
app.include_router(order_router)
app.include_router(revenue_router)
