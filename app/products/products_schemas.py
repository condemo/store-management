from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import uuid


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    id: int


class BrandResponse(BrandBase):
    id: int

    class Config:
        orm_mode = True


class ProductCategoryBase(BaseModel):
    name: str


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryUpdate(ProductCategoryBase):
    id: int


class ProductCategoryResponse(ProductCategoryBase):
    id: int

    class Config:
        orm_mode = True


class StockBase(BaseModel):
    qty: int


class StockRespone(StockBase):
    id: int
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class DiscountBase(BaseModel):
    name: str
    discount_percent: int


class DiscountCreate(DiscountBase):
    desc: Optional[str] = None
    active: Optional[bool] = False


class DiscountUpdate(BaseModel):
    id: int
    active: bool


class DiscountResponse(DiscountBase):
    id: int
    desc: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    active: bool

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    category_id: int
    brand_id: int
    provider_price: float


class ProductCompleteResponse(ProductBase):
    id: int
    category: ProductCategoryResponse
    provider_price: Optional[float] = None
    brand: BrandResponse
    stock: StockRespone
    uuid: uuid.UUID
    discount: Optional[DiscountResponse] = None
    created_at: datetime

    class Config:
        orm_mode = True


class ProductMinResponse(ProductBase):
    id: int
    provider_price: Optional[float] = None

    class Config:
        orm_mode = True


class ProductResponse(ProductBase):
    id: int
    category_id: int
    brand_id: int
    stock_id: int
    provider_price: Optional[float] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
