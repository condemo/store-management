from fastapi import APIRouter


router = APIRouter(
        prefix="/products",
        tags=["Products"]
        )


@router.get("/")
async def get_all_products():
    return
