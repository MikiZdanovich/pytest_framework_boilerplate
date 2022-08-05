import pytest
from requests import request
from src.utils.url_parser import set_url


def _get_pets_by_status(status='available'):
    response = request('GET', set_url('pet/findByStatus'), params={"status": status})
    return response


@pytest.fixture
def get_pets_by_status():
    return _get_pets_by_status
