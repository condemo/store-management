from sqlalchemy import Column, Integer, String
from ..database import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    contact_name = Column(String)
    phone = Column(String)
    web_url = Column(String)
