from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def get_list(cls):
        return [e.value for e in cls]

    @classmethod
    def get_keys(cls):
        return [e.name for e in cls]
