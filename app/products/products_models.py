from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float)
    category_id = mapped_column(ForeignKey("products_category.id", ondelete="CASCADE"))
    brand_id = mapped_column(ForeignKey("brands.id", ondelete="CASCADE"))
    stock_id = mapped_column(ForeignKey("stock.id", ondelete="CASCADE"), unique=True)
    discount_id = mapped_column(ForeignKey("discounts.id", ondelete="CASCADE"),
            nullable=True)
    uuid = Column(UUID(as_uuid=True), unique=True,
              nullable=False, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    category = relationship("ProductCategory", back_populates="products")
    brand = relationship("Brand", back_populates="products")
    stock = relationship("Stock", back_populates="product")
    discount = relationship("Discount", back_populates="product")
    listed = relationship("ProductListed", back_populates="product")


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    products = relationship("Product", back_populates="brand")


class ProductCategory(Base):
    __tablename__ = "products_category"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    products = relationship("Product", back_populates="category")


class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    desc = Column(String(1000), nullable=True)
    discount_percent = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    product = relationship("Product", back_populates="discount")


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, nullable=False, primary_key=True)
    qty = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    product = relationship("Product", back_populates="stock")
