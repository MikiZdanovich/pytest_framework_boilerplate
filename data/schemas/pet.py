from pydantic import BaseModel, validator, Field
from typing import List
from data.schemas.category import CategorySchema
from data.schemas.tag import TagSchema

from data.enums.pet_status import PetStatus


class PetSchema(BaseModel):
    id: int = None
    category: CategorySchema = Field(default_factory=CategorySchema)
    name: str = None
    photoUrls: List[str] = None
    tags: List[TagSchema] = None
    status: PetStatus = Field(...)
