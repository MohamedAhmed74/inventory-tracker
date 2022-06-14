from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from pydantic import BaseModel

if TYPE_CHECKING:
    pass


class BaseWarehouse(BaseModel):
    name: Optional[str]
    location: Optional[str]


class WarehouseCreate(BaseWarehouse):
    name: str
    location: str


class WarehouseUpdate(BaseWarehouse):
    pass


class WarehouseInDBBase(BaseWarehouse):
    id: int
    name: str
    location: str

    class Config:
        orm_mode = True


class Warehouse(WarehouseInDBBase):
    pass


class WarehouseInDB(WarehouseInDBBase):
    pass
