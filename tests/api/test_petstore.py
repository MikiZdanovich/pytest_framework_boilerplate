import pytest
from src.base.api.base_response import BaseResponse
from data.test_data.builders.pet_builder import PetBuilder


@pytest.mark.api
@pytest.mark.petstore
class PetStoreSuite:
    """This is sample test case"""

    @pytest.fixture
    def default_pet(self):
        return PetBuilder().set_defaults().build()

    def test_get_pet_by_id(self, get_pets_by_status):
        """This is sample test case"""
        response = BaseResponse(get_pets_by_status('available'))
        response.validate_status_code(200)

    def test_create_pet(self, create_pet, default_pet):
        """This is sample test case"""

        response = BaseResponse(create_pet(default_pet))

        response.validate_status_code(200)

        response.validate_json_response_body_field('name', default_pet['name'])
        response.validate_json_response_body_field('status', default_pet['status'])
        response.validate_json_response_body_field(('category', 'name'), default_pet['category']['name'])
        response.validate_json_response_body_field('photoUrls', default_pet['photoUrls'])
        response.validate_json_response_body_field(('tags', 'name'), default_pet['tags'][0]['name'])
