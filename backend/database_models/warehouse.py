from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from ..database import Base


class Warehouse(Base):
    __tablename__ = "warehouse"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    inventory = relationship("Inventory", back_populates="warehouse")
