from pydantic import BaseModel, validator, Field


class CategorySchema(BaseModel):
    id: int = None
    name: str = None
