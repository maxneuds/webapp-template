from pydantic import BaseModel


class DemoItem(BaseModel):
    name: str
    value: float

class DemoResponse(DemoItem):
    id: str


