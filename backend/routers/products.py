from fastapi import APIRouter, Depends

from schemas import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    DeleteProductResponse
)

from services.product_service import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product
)

from utils.dependencies import (
    get_current_user,
    require_admin
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get(
    "",
    response_model=list[ProductResponse]
)
async def get_all_products(
    current_user: dict = Depends(get_current_user)
):
    return await get_products()


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
async def get_product_detail(
    product_id: str,
    current_user: dict = Depends(get_current_user)
):
    return await get_product(product_id)


@router.post(
    "",
    response_model=ProductResponse
)
async def create_new_product(
    product_data: ProductCreate,
    current_user: dict = Depends(require_admin)
):
    return await create_product(product_data)


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
async def update_existing_product(
    product_id: str,
    product_data: ProductUpdate,
    current_user: dict = Depends(require_admin)
):
    return await update_product(
        product_id,
        product_data
    )


@router.delete(
    "/{product_id}",
    response_model=DeleteProductResponse
)
async def delete_existing_product(
    product_id: str,
    current_user: dict = Depends(require_admin)
):
    return await delete_product(product_id)