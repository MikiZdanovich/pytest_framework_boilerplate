from pydantic import BaseModel, validator, Field


class TagSchema(BaseModel):
    id: int = None
    name: str = None
