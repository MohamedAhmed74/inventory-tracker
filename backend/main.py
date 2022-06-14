import uvicorn
from fastapi import FastAPI

from backend.database import Base, engine
from backend.routers import inventory
from backend.routers import warehouse

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(inventory.router)
app.include_router(warehouse.router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", reload=True)
