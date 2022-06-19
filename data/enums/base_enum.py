from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def get_all(cls):
        return [e.value for e in cls]
