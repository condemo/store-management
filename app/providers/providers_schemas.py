from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class ProviderBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    contact_name: Optional[str] = None
    phone: Optional[str] = None
    web_url: Optional[str] = None


class ProviderCreate(ProviderBase):
    pass


class ProviderUpdate(ProviderBase):
    id: int


class ProviderResponse(ProviderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# PROVIDER ORDERS
class ProviderOrderBase(BaseModel):
    received: Optional[bool] = False
    paid: Optional[bool] = False
    provider_ticket_id: Optional[str] = None
    approx_delivery_date: Optional[date] = None


class ProviderOrderCreate(ProviderOrderBase):
    provider_id: int


class ProviderOrderUpdate(ProviderOrderBase):
    id: int


class ProviderOrderResponse(ProviderOrderBase):
    id: int
    provider: ProviderResponse
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
