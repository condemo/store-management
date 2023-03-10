from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import mapped_column, relationship
from ..database import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(50), unique=True)
    contact_name = Column(String(30))
    phone = Column(String(25))
    web_url = Column(String(100))
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("ProviderOrder", back_populates="provider")


class ProviderOrder(Base):
    __tablename__ = "provider_orders"

    id = Column(Integer, nullable=False, primary_key=True)
    provider_id = mapped_column(ForeignKey("providers.id", ondelete="CASCADE"), nullable=False)
    received = Column(Boolean, nullable=False)
    paid = Column(Boolean, nullable=False)
    provider_ticket_id = Column(String(50))
    approx_delivery_date = Column(Date)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    provider = relationship("Provider", back_populates="orders")
    products_listed = relationship("ProductListed", back_populates='order')


class ProductListed(Base):
    __tablename__ = "products_listed"

    order_id = mapped_column(ForeignKey("provider_orders.id", ondelete="CASCADE"),
                             nullable=False, primary_key=True)
    product_id = mapped_column(ForeignKey("products.id", ondelete="CASCADE"),
                               nullable=False, primary_key=True)
    qty = Column(Integer, nullable=False, default=0)

    order = relationship("ProviderOrder", back_populates="products_listed")
    product = relationship("Product", back_populates="listed")
