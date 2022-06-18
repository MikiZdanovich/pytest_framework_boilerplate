import os
from urllib.parse import urljoin
from src.exceptions.custom_exceptions import EnvironmentVariableExceptiom

def set_url(url):
    """ This function sets URL. """

    if url and url.startswith('http'):
        return url
    else:
        try:
            base_url = os.environ['BASE_URL']
        except KeyError:
            raise Exception('BASE_URL environment variable is not set!')

        if not url:
            url = base_url
        elif not url.startswith('http'):
            url = urljoin(base_url, url)
        return url
