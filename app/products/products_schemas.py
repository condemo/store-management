from datetime import datetime
from typing import Optional
from pydantic import BaseModel


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


class ProductBase(BaseModel):
    name: str
    price: Optional[float] = None


class ProductCreate(ProductBase):
    category_id: int
    brand_id: int


class ProductResponse(ProductBase):
    id: int
    category_id: int
    brand_id: int
    stock: StockRespone
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    id: int
    category_id: int
    brand_id: int
