from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from .. import products_models, products_schemas


router = APIRouter(
        prefix="/category",
        )


@router.get("/", response_model=List[products_schemas.ProductCategoryResponse])
async def get_categories(db: Session = Depends(get_db)):
    category_list = db.query(products_models.ProductCategory).all()

    return category_list


@router.get("/{id}", response_model=products_schemas.ProductCategoryResponse)
async def get_one_category(id: int, db: Session = Depends(get_db)):
    category = db.query(products_models.ProductCategory).filter(
            products_models.ProductCategory.id == id
            ).first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The category with id {id} is not found")

    return category


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=products_schemas.ProductCategoryResponse)
async def create_category(category: products_schemas.ProductCategoryCreate,
                          db: Session = Depends(get_db)):
    new_category = products_models.ProductCategory(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


@router.put("/")
async def update_category(updated_category: products_schemas.ProductCategoryUpdate,
                          db: Session = Depends(get_db)):
    category_query = db.query(products_models.ProductCategory).filter(
            products_models.ProductCategory.id == updated_category.id
            )
    category = category_query.first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The category with id {id} is not found")

    category_query.update(updated_category.dict(), synchronize_session=False)
    db.commit()

    return category_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int, db: Session = Depends(get_db)):
    category_query = db.query(products_models.ProductCategory).filter(
            products_models.ProductCategory.id == id
            )
    category = category_query.first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The category with id {id} is not found")

    category_query.delete(synchronize_session=False)
    db.commit()

    return category_query.first()
