from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import mapped_column, relationship
from ..database import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    contact_name = Column(String)
    phone = Column(String)
    web_url = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("ProviderOrder", back_populates="provider")


class ProviderOrder(Base):
    __tablename__ = "provider_orders"

    id = Column(Integer, nullable=False, primary_key=True)
    provider_id = mapped_column(ForeignKey("providers.id", ondelete="CASCADE"), nullable=False)
    received = Column(Boolean, nullable=False)
    paid = Column(Boolean, nullable=False)
    provider_ticket_id = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    provider = relationship("Provider", back_populates="orders")
