from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from typing import List

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float)
    category_id: Mapped[int] = mapped_column(ForeignKey("products_category.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    stock_id: Mapped[int] = mapped_column(ForeignKey("stock.id"))
    uuid = Column(UUID(as_uuid=True), unique=True,
              nullable=False, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    stock: Mapped["Stock"] = relationship(back_populates="product")


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    products: Mapped[List[Product]] = relationship()


class ProductCategory(Base):
    __tablename__ = "products_category"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    products: Mapped[List[Product]] = relationship()


class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    desc = Column(String, nullable=True)
    discount_percent = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        onupdate=func.now())


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, nullable=False, primary_key=True)
    qty = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    product: Mapped["Product"] = relationship(back_populates="stock")
