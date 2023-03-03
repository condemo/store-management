from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ...database import get_db
from .. import products_schemas, products_models


router = APIRouter(
        prefix="/brands",
        )


@router.get("/", response_model=List[products_schemas.BrandResponse])
async def get_all_brands(limit: int = 10, search: Optional[str] = "",
                         db: Session = Depends(get_db)):
    brand_list = db.query(products_models.Brand) \
            .filter(products_models.Brand.name.ilike(f"%{search}%")) \
            .limit(limit).all()

    return brand_list


@router.get("/{id}", response_model=products_schemas.BrandResponse)
async def get_one_brand(id: int, db: Session = Depends(get_db)):
    brand = db.query(products_models.Brand).filter(
            products_models.Brand.id == id).first()

    if not brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The brand with id {id} is not found")

    return brand


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.BrandResponse)
async def create_brand(brand: products_schemas.BrandCreate,
                       db: Session = Depends(get_db)):
    new_brand = products_models.Brand(**brand.dict())
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


@router.put("/", response_model=products_schemas.BrandResponse)
async def update_brand(updated_brand: products_schemas.BrandUpdate,
                       db: Session = Depends(get_db)):
    brand_query = db.query(products_models.Brand).filter(
            products_models.Brand.id == updated_brand.id
            )
    brand = brand_query.first()

    if not brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The brand with id {id} is not found")

    brand_query.update(updated_brand.dict(), synchronize_session=False)
    db.commit()

    return brand_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(id: int, db: Session = Depends(get_db)):
    brand_query = db.query(products_models.Brand).filter(
            products_models.Brand.id == id
            )
    brand = brand_query.first()

    if not brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The brand with id {id} is not found")

    brand_query.delete(synchronize_session=False)
    db.commit()

    return
