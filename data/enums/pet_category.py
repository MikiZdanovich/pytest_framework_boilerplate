from data.enums.base_enum import BaseEnum


class PetCategory(BaseEnum):
    dog = 'dog'
    cat = 'cat'
    bird = 'bird'
    fish = 'fish'
    reptile = 'reptile'
    invertebrate = 'invertebrate'

    @classmethod
    def get_all(cls):
        return [e.value for e in cls]
