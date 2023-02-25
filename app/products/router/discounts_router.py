from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from .. import products_models, products_schemas


router = APIRouter(
        prefix="/discounts"
        )


@router.get("/", response_model=List[products_schemas.DiscountResponse])
async def get_discounts(db: Session = Depends(get_db)):
    discounts_list = db.query(products_models.Discount).all()

    return discounts_list


@router.get("/{id}", response_model=products_schemas.DiscountResponse)
async def get_one_discount(id: int, db: Session = Depends(get_db)):
    discount = db.query(products_models.Discount).filter(products_models.Discount.id == id).first()

    if not discount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The discount woth id {id} is not found")

    return discount


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.DiscountResponse)
async def create_discount(discount: products_schemas.DiscountCreate,
                          db: Session = Depends(get_db)):
    new_discount = products_models.Discount(**discount.dict())
    db.add(new_discount)
    db.commit()
    db.refresh(new_discount)

    return new_discount


@router.put("/", response_model=products_schemas.DiscountResponse)
async def update_discount(updated_discount: products_schemas.DiscountUpdate,
                          db: Session = Depends(get_db)):
    discount_query = db.query(products_models.Discount).filter(
            products_models.Discount.id == updated_discount.id)
    discount = discount_query.first()

    if not discount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The discount with id {id} is not found")

    discount_query.update(updated_discount.dict(), synchronize_session=False)
    db.commit()

    return discount_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_discount(id: int, db: Session = Depends(get_db)):
    discount_query = db.query(products_models.Discount).filter(products_models.Discount.id == id)
    discount = discount_query.first()

    if not discount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The discount with id {id} is not found")

    discount_query.delete(synchronize_session=False)
    db.commit()

    return discount_query.first()