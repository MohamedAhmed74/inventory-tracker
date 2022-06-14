from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel

from backend.pydantic_models.warehouse import Warehouse

if TYPE_CHECKING:
    pass


class BaseInventory(BaseModel):
    name: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    description: Optional[str]


class InventoryCreate(BaseInventory):
    name: str
    price: float
    quantity: int


class InventoryUpdate(BaseInventory):
    warehouse_id: Optional[int]


class InventoryInDBBase(BaseInventory):
    id: int
    name: str
    price: float
    quantity: int

    warehouse: Optional[Warehouse]

    class Config:
        orm_mode = True


class Inventory(InventoryInDBBase):
    pass


class InventoryInDB(InventoryInDBBase):
    pass
