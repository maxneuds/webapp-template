from app.db import database
from app.schemas.demo import DemoItem, DemoResponse


class DemoService:
    @staticmethod
    async def create_item(item: DemoItem) -> DemoResponse:
        result = await database["demo"].insert_one(item.model_dump())
        return DemoResponse(id=str(result.inserted_id), **item.model_dump())

    @staticmethod
    async def list_items() -> list[DemoResponse]:
        items = await database["demo"].find().to_list(100)
        return [DemoResponse(id=str(item["_id"]), **item) for item in items]


