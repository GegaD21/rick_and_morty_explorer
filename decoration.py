import time
from functools import wraps

import requests

from exception import APIException


def handle_api_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except requests.Timeout as error:
            raise APIException(
                "Request timed out. Please try again."
            ) from error

        except requests.ConnectionError as error:
            raise APIException(
                "Could not connect to Rick and Morty API."
            ) from error

        except requests.HTTPError as error:
            raise APIException(
                f"API returned an HTTP error: {error}"
            ) from error

        except requests.RequestException as error:
            raise APIException(
                "API request failed. Please try again."
            ) from error

    return wrapper


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except requests.RequestException as error:
                    last_error = error

                    if attempt < max_attempts - 1:
                        time.sleep(delay)

            raise last_error

        return wrapper

    return decorator
