from faker import Faker

from data.test_data.base_generator import BaseGenerator
from data.test_data.providers.fake_providers import pet_status_provider


class StatusGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self._seed()

    def set_pet_status(self, status=None):
        if not status:
            fake = Faker()
            fake.add_provider(pet_status_provider)
            status = fake.pet_status()
        self.result['status'] = status
        return self

    def _seed(self):
        self.set_pet_status()
