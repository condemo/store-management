from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float)
    uuid = Column(UUID(as_uuid=True), unique=True,
              nullable=False, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class ProductCategory(Base):
    __tablename__ = "products_category"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)


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
