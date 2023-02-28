from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...database import get_db
from .. import providers_models, providers_schemas


router = APIRouter(
        prefix="/orders",
        )


@router.get("/", response_model=list[providers_schemas.ProviderOrderResponse])
async def get_provider_orders(db: Session = Depends(get_db)):
    order_list = db.query(providers_models.ProviderOrder).all()

    return order_list


@router.get("/{id}", response_model=providers_schemas.ProviderResponse)
async def get_one_order(id: int, db: Session = Depends(get_db)):
    order = db.query(providers_models.ProviderOrder) \
            .filter(providers_models.ProviderOrder.id == id) \
            .first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The order with id {id} is not found")

    return order


@router.post("/", response_model=providers_schemas.ProviderOrderResponse,
             status_code=status.HTTP_201_CREATED)
async def create_provider_order(provider_order: providers_schemas.ProviderOrderCreate,
                                db: Session = Depends(get_db)):
    new_order = providers_models.ProviderOrder(**provider_order.dict())

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.put("/", response_model=providers_schemas.ProviderOrderResponse)
async def update_provider_order(updated_order: providers_schemas.ProviderOrderUpdate,
                                db: Session = Depends(get_db)):
    order_query = db.query(providers_models.ProviderOrder) \
            .filter(providers_models.ProviderOrder.id == updated_order.id)
    order = order_query.first()

    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The order with id {id} is not found")

    order_query.update(updated_order.dict(), synchronize_session=False)
    db.commit()

    return order_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_provider_order(id: int, db: Session = Depends(get_db)):
    order_query = db.query(providers_models.ProviderOrder) \
            .filter(providers_models.ProviderOrder.id == id)
    order = order_query.first()

    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The order with id {id} is not found")

    order_query.delete(synchronize_session=False)
    db.commit()

    return
