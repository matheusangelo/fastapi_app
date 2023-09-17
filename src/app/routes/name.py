from fastapi import APIRouter
from app.models import EnumName
from app.services import get_model_names


name_router = APIRouter(
    prefix="/name",
    tags=['Names']
)


@name_router.get("/models/{model_name}")
async def get_model(model_name: EnumName):
    return get_model_names(model_name)
