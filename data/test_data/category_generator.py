from faker import Faker

from data.test_data.base_generator import BaseGenerator
from data.test_data.providers.fake_providers import pet_categories_provider


class CategoryGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self._seed()

    def set_category_name(self, cat_name=None):
        if not cat_name:
            fake = Faker()
            fake.add_provider(pet_categories_provider)
            cat_name = fake.pet_category()
        self.result['name'] = cat_name
        return self

    def _seed(self):
        self.set_category_name()
