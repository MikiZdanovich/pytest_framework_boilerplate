import pytest
from requests import request
from src.base.base_response import BaseResponse
from data.schemas.pet import PetSchema

@pytest.mark.api
@pytest.mark.petstore
class PetstoreSuite:
    """This is sample test case"""

    def test_get_pet_by_id(self):
        """This is sample test case"""
        response = request('GET', 'http://petstore.swagger.io/v2/pet/findByStatus?status=available')
        response = BaseResponse(response)
        response.validate_status_code(200).validate_response_schema(PetSchema)


