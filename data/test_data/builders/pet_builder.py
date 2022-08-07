from faker import Faker
from src.base.test_data.base_builder import BaseBuilder
from data.enums.pet_status_enum import PetStatus


class PetBuilder(BaseBuilder):
    def __init__(self):
        super().__init__()
        self.fake = Faker()

    def set_name(self, name=None):
        if not name:
            name = self.fake.first_name()
        self.data['name'] = name
        return self

    def set_status(self, status=None):
        if not status:
            status = self.fake.random_element(PetStatus.get_all())
        self.data['status'] = status
        return self

    def set_category(self, category=None):
        if not category:
            category = self.fake.color_name()
        self.data['category'] = {"name": category}
        return self

    def set_tags(self, tags=None):
        if not tags:
            tags = self.fake.color_name()
        if isinstance(tags, str):
            self.data['tags'] = [{'name': tags}]
        elif isinstance(tags, list):
            self.data['tags'] = [{'name': tag} for tag in tags]
        return self

    def set_photo_urls(self, photo_urls=None):
        if not photo_urls:
            photo_urls = self.fake.image_url()
        if isinstance(photo_urls, str):
            self.data['photoUrls'] = [photo_urls]
        elif isinstance(photo_urls, list):
            self.data['photo_urls'] = [url for url in photo_urls]
        return self

    def set_defaults(self):
        self.set_name()
        self.set_status()
        self.set_category()
        self.set_tags()
        self.set_photo_urls()
        return self
