from fastapi import APIRouter
from .migration_controller import router as migration
from .authentification_controller import router as authentication
from .user_controller import router as user
from .storage_controller import router as storage
from .address_controller import router as address
from .category_blog_controlleur import router as category_blog
from .client_controleur import router as client
from .product_controlleur import router as product
from .sell_product_controlleur import router as sell_product
api_router = APIRouter()

api_router.include_router(migration)
api_router.include_router(authentication)
api_router.include_router(user)
api_router.include_router(storage)
api_router.include_router(address)
api_router.include_router(category_blog)
api_router.include_router(client)
api_router.include_router(product)
api_router.include_router(sell_product)