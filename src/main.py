
from fastapi import FastAPI
from app.routes import item_router, name_router


app = FastAPI()

app.include_router(item_router)
app.include_router(name_router)

