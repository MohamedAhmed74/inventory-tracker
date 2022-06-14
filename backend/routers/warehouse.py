from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List

from backend.database import get_db
from backend import database_models
from backend.pydantic_models.warehouse import Warehouse, WarehouseUpdate, WarehouseCreate

router = APIRouter(
    tags=["warehouse"],
    prefix="/warehouse"
)


@router.get('/', response_model=List[Warehouse])
def get_all(db: Session = Depends(get_db)):
    return db.query(database_models.Warehouse).all()


@router.get('/{warehouse_id}', response_model=Warehouse)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return db.query(database_models.Warehouse).filter(database_models.Warehouse.id == warehouse_id).first()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Warehouse)
def create(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    new_warehouse = database_models.Warehouse(
        name=warehouse.name,
        location=warehouse.location
    )
    db.add(new_warehouse)
    db.commit()
    db.refresh(new_warehouse)
    return new_warehouse


@router.patch('/{warehouse_id}', status_code=status.HTTP_202_ACCEPTED, response_model=Warehouse)
def update(warehouse_id: int, data: WarehouseUpdate, db: Session = Depends(get_db)):
    warehouse = db.query(database_models.Warehouse).filter(database_models.Warehouse.id == warehouse_id).first()

    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {warehouse_id} not found")

    for column, value in data.dict(exclude_unset=True).items():
        setattr(warehouse, column, value)

    db.commit()
    db.refresh(warehouse)
    return warehouse


@router.delete('/{warehouse_id}', status_code=status.HTTP_202_ACCEPTED, response_model=Warehouse)
def destroy(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse = db.query(database_models.Warehouse).filter(database_models.Warehouse.id == warehouse_id).first()

    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {warehouse_id} not found")

    db.delete(warehouse)
    db.commit()
    return warehouse
