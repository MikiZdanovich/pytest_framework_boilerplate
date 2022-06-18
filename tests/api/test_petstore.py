import pytest
from src.base.api.base_response import BaseResponse
from data.schemas.pet import PetSchema


@pytest.mark.api
@pytest.mark.petstore
class PetstoreSuite:
    """This is sample test case"""

    def test_get_pet_by_id(self, get_pets_by_status):
        """This is sample test case"""

        response = BaseResponse(get_pets_by_status('available'))
        response.validate_status_code(20).validate_response_schema(PetSchema)
