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
