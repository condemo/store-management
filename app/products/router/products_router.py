from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from . import brands_router, category_router, discounts_router
from .. import products_schemas, products_models

# TODO: Chequear las dependencias de una ruta general

router = APIRouter(
        prefix="/products",
        tags=["Products"]
        )


router.include_router(brands_router.router)
router.include_router(category_router.router)
router.include_router(discounts_router.router)


@router.get("/", response_model=list[products_schemas.ProductCompleteResponse])
async def get_products(limit: int = 10, search: Optional[str] = "",
                       db: Session = Depends(get_db)):
    results = db.query(products_models.Product).join(
        products_models.Stock, products_models.Stock.id == products_models.Product.stock_id,
        isouter=True).join(
        products_models.ProductCategory,
        products_models.ProductCategory.id == products_models.Product.category_id,
        isouter=True).join(
        products_models.Brand,
        products_models.Brand.id == products_models.Product.brand_id,
        isouter=True).join(
                products_models.Discount,
                products_models.Discount.id == products_models.Product.discount_id,
                isouter=True).filter(products_models.Product.name.ilike(f"%{search}%")) \
                        .group_by(products_models.Product.id).limit(limit).all()

    return results


@router.get("/{id}", response_model=products_schemas.ProductCompleteResponse)
async def get_one_product(id: int, db: Session = Depends(get_db)):
    product = db.query(products_models.Product).join(
        products_models.Stock, products_models.Stock.id == products_models.Product.stock_id,
        isouter=True).join(
        products_models.ProductCategory,
        products_models.ProductCategory.id == products_models.Product.category_id,
        isouter=True).join(
        products_models.Brand,
        products_models.Brand.id == products_models.Product.brand_id,
        isouter=True).join(
                products_models.Discount,
                products_models.Discount.id == products_models.Product.discount_id,
                isouter=True).group_by(
        products_models.Product.id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The product with id {id} is not found")

    return product


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.ProductCompleteResponse)
async def create_product(new_product: products_schemas.ProductCreate,
                         qty: Optional[int] = 0, db: Session = Depends(get_db)):
    new_stock = products_models.Stock(qty=qty)
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)

    product = products_models.Product(**new_product.dict(), stock_id=new_stock.id)
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@router.put("/price-update", response_model=products_schemas.ProductCompleteResponse)
async def update_product_price(id: int, price: float,
                               db: Session = Depends(get_db)):
    product_query = db.query(products_models.Product) \
            .filter(products_models.Product.id == id)
    product = product_query.first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The product with id {id} is not found")
    product_query.update({"price": price})
    db.commit()

    return product_query.first()


@router.put("/stock-update")
async def update_product_stock(id: int, qty: int, db: Session = Depends(get_db)):
    stock_query = db.query(products_models.Stock) \
            .filter(products_models.Stock.id == id)
    stock = stock_query.first()

    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Stock record with id {id} is not found")
    stock_query.update({"qty": stock.qty + qty}, synchronize_session=False)
    db.commit()

    return stock_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int, db: Session = Depends(get_db)):
    product_query = db.query(products_models.Product).filter(products_models.Product.id == id)
    product = product_query.first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The prodcut with id {id} is not found")

    product_query.delete(synchronize_session=False)
    db.commit()

    return
