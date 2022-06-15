from pydantic import BaseModel, validator, Field
from typing import List
from data.schemas.category import CategorySchema
from data.schemas.tag import TagSchema

from data.schemas.status import StatusSchema


class PetSchema(BaseModel):
    id: int = None
    category: CategorySchema = Field(None, alias='category')
    name: str = None
    photoUrls: List[str]
    tags: List[TagSchema] = None
    status: StatusSchema = Field(...)

