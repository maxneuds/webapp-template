from fastapi import APIRouter, HTTPException
from app.schemas.demo import DemoItem, DemoResponse
from app.services.demo import DemoService
# Set prefix and tags for the router
router = APIRouter(prefix="/demo", tags=["demo"])


# create 
@router.post("/", response_model=DemoResponse)
async def create_item(item: DemoItem):
    return await DemoService.create_item(item)

@router.get("/", response_model=list[DemoResponse])
async def list_items():
    return await DemoService.list_items()


