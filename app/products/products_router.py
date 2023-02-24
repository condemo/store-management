from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database import get_db
from . import products_schemas, products_models


router = APIRouter(
        prefix="/products",
        tags=["Products"]
        )


@router.get("/brands", response_model=List[products_schemas.BrandResponse])
async def get_all_brands(db: Session = Depends(get_db)):
    brand_list = db.query(products_models.Brand).all()

    return brand_list


@router.get("/brands/{id}", response_model=products_schemas.BrandResponse)
async def get_one_brand(id: int, db: Session = Depends(get_db)):
    brand = db.query(products_models.Brand).filter(
            products_models.Brand.id == id).first()

    return brand


@router.post("/brands", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.BrandResponse)
async def create_brand(brand: products_schemas.BrandCreate,
                       db: Session = Depends(get_db)):
    new_brand = products_models.Brand(**brand.dict())
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


@router.put("/brands", response_model=products_schemas.BrandResponse)
async def update_brand(updated_brand: products_schemas.BrandUpdate,
                       db: Session = Depends(get_db)):
    brand_query = db.query(products_models.Brand).filter(
            products_models.Brand.id == updated_brand.id
            )
    brand = brand_query.first()
    # TODO: Error management check brands
    brand_query.update(updated_brand.dict(), synchronize_session=False)
    db.commit()

    return brand_query.first()


@router.delete("/brands/{id}")
async def delete_brand(id: int, db: Session = Depends(get_db)):
    brand_query = db.query(products_models.Brand).filter(
            products_models.Brand.id == id
            )
    brand = brand_query.first()
    # TODO: Error management
    brand_query.delete(synchronize_session=False)

    return brand_query.first()
