from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from . import brands_router, category_router
from .. import products_schemas, products_models

# TODO: Chequear las dependencias de una ruta general

router = APIRouter(
        prefix="/products",
        tags=["Products"]
        )


router.include_router(brands_router.router)
router.include_router(category_router.router)


@router.get("/", response_model=List[products_schemas.ProductResponse])
async def get_products(db: Session = Depends(get_db)):
    results = db.query(products_models.Product).join(
        products_models.Stock, products_models.Stock.id == products_models.Product.stock_id,
        isouter=True).group_by(
        products_models.Product.id).all()

    return results


@router.get("/{id}", response_model=products_schemas.ProductResponse)
async def get_one_product(id: int, db: Session = Depends(get_db)):
    product = db.query(products_models.Product).filter(
            products_models.Product.id == id
            ).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The product with id {id} is not found")

    return product


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.ProductResponse)
async def create_product(new_product: products_schemas.ProductCreate,
                         db: Session = Depends(get_db)):
    new_stock = products_models.Stock(qty=0)
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)

    product = products_models.Product(**new_product.dict(), stock_id=new_stock.id)
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@router.put("/")
async def update_product(updated_product: products_schemas.ProductUpdate,
                         db: Session = Depends(get_db)):
    return


@router.delete("/{id}")
async def delete_product(id: int, db: Session = Depends(get_db)):
    return
