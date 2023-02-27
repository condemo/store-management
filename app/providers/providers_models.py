from sqlalchemy import Column, DateTime, Integer, String, func
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
