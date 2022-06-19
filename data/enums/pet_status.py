from data.enums.base_enum import BaseEnum


class PetStatus(BaseEnum):
    available = 'available'
    pending = 'pending'
    sold = 'sold'

    @classmethod
    def get_all(cls):
        return [e.value for e in cls]
