from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int = None
    name: str = None
