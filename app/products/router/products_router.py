from fastapi import APIRouter

from . import brands_router

# TODO: Chequear las dependencias de una ruta general

router = APIRouter(
        prefix="/products",
        tags=["Products"]
        )


@router.get("/")
async def root():
    return


router.include_router(brands_router.router)
