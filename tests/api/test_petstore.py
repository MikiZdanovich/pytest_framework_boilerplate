import pytest
from src.base.api.base_response import BaseResponse


@pytest.mark.api
@pytest.mark.petstore
class PetStoreSuite:
    """This is sample test case"""

    def test_get_pet_by_id(self, get_pets_by_status):
        """This is sample test case"""
        response = BaseResponse(get_pets_by_status('available'))
        response.validate_status_code(20)
