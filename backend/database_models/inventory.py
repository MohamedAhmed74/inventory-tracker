from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    warehouse_id = Column(Integer, ForeignKey("warehouse.id"), nullable=True)

    warehouse = relationship("Warehouse", lazy='joined', back_populates="inventory")
