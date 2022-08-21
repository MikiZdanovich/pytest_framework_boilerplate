import pytest
from src.base.api.http_client import RequestHandler


def _get_pets_by_status(status='available'):
    params = {"status": status}
    return RequestHandler.get('pet/findByStatus', params=params)


def _create_pet(pet):
    return RequestHandler.post('pet', json=pet)


@pytest.fixture
def get_pets_by_status():
    return _get_pets_by_status


@pytest.fixture
def create_pet():
    return _create_pet
