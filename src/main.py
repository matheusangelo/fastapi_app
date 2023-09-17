
from fastapi import FastAPI
from app.routes import item_router


app = FastAPI()

app.include_router(item_router)
