from fastapi import APIRouter
from app.models import EnumName
from app.services import get_all_items, get_model_names


item_router = APIRouter(
    prefix="/items",
    tags=['Items']
)


@item_router.get("/")
async def read_item(skip: int = 0, limit: int = 10):
    items = get_all_items()
    return items[skip : skip + limit]


@item_router.get("/models/{model_name}")
async def get_model(model_name: EnumName):
    return get_model_names(model_name)