import requests
from exception import APIException


def handle_api_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            raise APIException("API request failed") from e

    return wrapper
