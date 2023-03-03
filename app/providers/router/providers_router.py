from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session


from ...database import get_db
from .. import providers_models, providers_schemas
from . import provider_orders_router


router = APIRouter(
        prefix="/providers",
        tags=["Providers"]
        )

router.include_router(provider_orders_router.router)


@router.get("/", response_model=list[providers_schemas.ProviderResponse])
async def get_providers(limit: int = 10, search: Optional[str] = "",
                        db: Session = Depends(get_db)):
    providers_list = db.query(providers_models.Provider) \
            .filter(providers_models.Provider.name.ilike(f"%{search}%")) \
            .limit(limit) \
            .all()

    return providers_list


@router.get("/{id}")
async def get_one_provider(id: int, db: Session = Depends(get_db)):
    provider = db.query(providers_models.Provider) \
            .filter(providers_models.Provider.id == id).first()

    if not provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The Provider with id {id} is not found")

    return provider


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=providers_schemas.ProviderResponse)
async def create_provider(provider: providers_schemas.ProviderCreate,
                          db: Session = Depends(get_db)):
    new_provider = providers_models.Provider(**provider.dict())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)

    return new_provider


@router.put("/")
async def update_provider(updated_provider: providers_schemas.ProviderUpdate,
                          db: Session = Depends(get_db)):
    provider_query = db.query(providers_models.Provider) \
            .filter(providers_models.Provider.id == updated_provider.id)
    provider = provider_query.first()

    if not provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The provider with id {id} is not found")

    provider_query.update(updated_provider.dict(), synchronize_session=False)
    db.commit()

    return provider_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_provider(id: int, db: Session = Depends(get_db)):
    provider_query = db.query(providers_models.Provider) \
            .filter(providers_models.Provider.id == id)
    provider = provider_query.first()

    if not provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The provider with id {id} is not found")

    provider_query.delete(synchronize_session=False)
    db.commit()

    return
