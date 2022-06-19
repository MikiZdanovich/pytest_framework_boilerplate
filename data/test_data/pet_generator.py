from data.test_data.base_generator import BaseGenerator
from data.test_data.category_generator import CategoryGenerator
from data.test_data.status_generator import StatusGenerator


class PetGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self._seed()

    def set_status(self, status=None):
        """
        :param status:
        :return:
        """
        if not status:
            status = StatusGenerator().build()

        self.result['status'] = status
        return self

    def set_category(self, category_name=None):
        if not category_name:
            category_name = CategoryGenerator().build()

        if isinstance(category_name, str):
            self.result['category']['name'] = category_name

        elif isinstance(category_name, BaseGenerator):
            self.result['category'] = category_name
        return self

    def set_name(self, name='Test'):
        """
        :param name:
        :return:
        """
        self.result['name'] = name
        return self

    def set_tags(self, tags=None):
        """
        :param tags: list dict or None
        :return: self
        """

        if tags is None:
            tags = {"name": 'tag1'}

        if isinstance(tags, dict):
            self.result['tags'] = [{name: tag} for name, tag in tags.items()]
        elif isinstance(tags, list):
            self.result['tags'] = tags
        return self

    def _seed(self):
        self.set_name().set_tags().set_category().set_status()
