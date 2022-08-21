import os
from urllib.parse import urljoin
from src.exceptions.custom_exceptions import EnvironmentVariableException


def set_url(url: str) -> str:
    """
    This function sets URL.
    @param url: URL string. or endpoint string.
    @return: URL string.
    """

    if url and url.startswith('http'):
        return url
    else:
        try:
            base_url = os.environ['BASE_URL']
        except KeyError:
            raise EnvironmentVariableException('BASE_URL')

        if not url:
            url = base_url
        elif not url.startswith('http'):
            url = urljoin(base_url, url)
        return url
