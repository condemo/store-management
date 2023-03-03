from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from .. import providers_models, providers_schemas


router = APIRouter(
        prefix="/listed"
        )


@router.get("/all", response_model=list[providers_schemas.ProductListedResponse])
async def get_products_listed(db: Session = Depends(get_db)):
    list_products = db.query(providers_models.ProductListed).all()

    return list_products


@router.get("/", response_model=providers_schemas.ProductListedResponse)
async def get_one_product_listed(order_id: int, product_id: int, db: Session = Depends(get_db)):
    product = db.query(providers_models.ProductListed) \
            .filter(providers_models.ProductListed.order_id == order_id) \
            .filter(providers_models.ProductListed.product_id == product_id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The product with id {product_id} is not found in the order with id {order_id}")

    return product


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=list[providers_schemas.ProductListedResponse])
async def create_product_listed(products: list[providers_schemas.ProductListedCreate],
                                db: Session = Depends(get_db)):
    product_list = []
    for product in products:
        product_add = providers_models.ProductListed(**product.dict())
        db.add(product_add)
        db.commit()
        db.refresh(product_add)

        product_list.append(product_add)

    return product_list


@router.put("/")
async def update_product_listed(updated_product: providers_schemas.ProductListedUpdate,
                                db: Session = Depends(get_db)):
    product_query = db.query(providers_models.ProductListed) \
            .filter(providers_models.ProductListed.order_id == updated_product.order_id) \
            .filter(providers_models.ProductListed.product_id == updated_product.product_id)
    product = product_query.first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The product with id {updated_product.product_id} is not found \
                                    in the order with id {updated_product.order_id}")
    product_query.update(updated_product.dict(), synchronize_session=False)
    db.commit()

    return product_query.first()


@router.delete("/{order_id}/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_listed(order_id: int, product_id: int, db: Session = Depends(get_db)):
    product_query = db.query(providers_models.ProductListed) \
            .filter(providers_models.ProductListed.order_id == order_id) \
            .filter(providers_models.ProductListed.product_id == product_id)
    product = product_query.first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The listed product with id {id} is not found")
    product_query.delete(synchronize_session=False)
    db.commit()

    return
