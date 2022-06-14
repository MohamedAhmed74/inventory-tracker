from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List

from backend.database import get_db
from backend import database_models
from backend.pydantic_models.inventory import Inventory, InventoryUpdate, InventoryCreate

router = APIRouter(
    tags=["inventory"],
    prefix="/inventory"
)


@router.get('/', response_model=List[Inventory])
def get_all(db: Session = Depends(get_db)):
    return db.query(database_models.Inventory).all()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Inventory)
def create(item: InventoryCreate, db: Session = Depends(get_db)):
    new_item = database_models.Inventory(
        name=item.name,
        price=item.price,
        quantity=item.quantity,
        description=item.description
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.patch('/{item_id}', status_code=status.HTTP_202_ACCEPTED, response_model=Inventory)
def update(item_id: int, data: InventoryUpdate, db: Session = Depends(get_db)):
    item = db.query(database_models.Inventory).filter(database_models.Inventory.id == item_id).first()

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {item_id} not found")

    for column, value in data.dict(exclude_unset=True).items():
        setattr(item, column, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete('/{item_id}', status_code=status.HTTP_202_ACCEPTED, response_model=Inventory)
def destroy(item_id: int, db: Session = Depends(get_db)):
    item = db.query(database_models.Inventory).filter(database_models.Inventory.id == item_id).first()

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {item_id} not found")

    db.delete(item)
    db.commit()
    return item
