from fastapi import APIRouter
from app.models import Item
from app.services import get_all_items, create_item as create


item_router = APIRouter(
    prefix="/item",
    tags=['Items']
)


@item_router.get("/")
async def read_item(skip: int = 0, limit: int = 10):
    items = get_all_items()
    return items[skip : skip + limit]


@item_router.post("/")
async def create_item(item: Item):
    return create(item)