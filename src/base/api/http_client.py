from requests import request
from abc import ABC

from src.utils.url_parser import set_url


class BaseHttpHandler(ABC):
    """
    Base class for HTTP Handlers
    """


class RequestHandler(BaseHttpHandler):
    """
    Class for HTTP request handling
    """

    @staticmethod
    def post(endpoint: str, json, headers: dict = None, **kwargs):
        url = set_url(endpoint)
        return request(method='POST', url=url, headers=headers, json=json, **kwargs)

    @staticmethod
    def get(endpoint: str, headers: dict = None, params: dict = None, **kwargs):
        url = set_url(endpoint)
        return request(method='GET', url=url, headers=headers, params=params, **kwargs)
