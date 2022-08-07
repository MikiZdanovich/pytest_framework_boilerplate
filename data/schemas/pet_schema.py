from pydantic import BaseModel, HttpUrl
from pydantic.types import List

from data.enums.pet_status_enum import PetStatus
from category_schema import Category
from tag_schema import Tag


class Pet(BaseModel):
    name: str
    status: PetStatus
    category: Category
    tags: List[Tag]
    photoUrls: List[HttpUrl]


