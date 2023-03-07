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


class DiscountBase(BaseModel):
    name: str
    discount_percent: int
    active: Optional[bool] = False


class DiscountCreate(DiscountBase):
    desc: Optional[str] = None


class DiscountUpdate(BaseModel):
    id: int
    active: bool


class DiscountResponse(DiscountBase):
    id: int
    desc: Optional[str] = None
    created_at: datetime
    update_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: Optional[float] = None


class ProductCreate(ProductBase):
    category_id: int
    brand_id: int


class ProductCompleteResponse(ProductBase):
    id: int
    category: ProductCategoryResponse
    brand: BrandResponse
    stock: StockRespone
    discount: Optional[DiscountResponse] = None
    created_at: datetime

    class Config:
        orm_mode = True


class ProductMinResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductResponse(ProductBase):
    id: int
    category_id: int
    brand_id: int
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    id: int
    category_id: int
    discount_id: Optional[int] = None
    brand_id: int
