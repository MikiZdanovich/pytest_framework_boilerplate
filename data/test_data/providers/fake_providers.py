from faker.providers import DynamicProvider
from data.enums.pet_status import PetStatus
from data.enums.pet_category import PetCategory


pet_categories = PetCategory.get_all()
pet_status = PetStatus.get_all()

pet_status_provider = DynamicProvider(provider_name='pet_status', elements=pet_status)

pet_categories_provider = DynamicProvider(provider_name='pet_category',
                                          elements=pet_categories)
