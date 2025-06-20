from functools import lru_cache
from decouple import config


# currently none of these values need validation beyond they exist and what's listed here.
# if some validation is needed add it into utility/common_impl
class Settings:
    PROJECT_NAME: str = config("PROJECT_NAME")
    API_V1_STR: str = "/api/v1"
    def __init__(self):
        pass

@lru_cache
def get_settings():
    return Settings()


def format_url(url: str):
    if url and url.endswith("/"):
        return url[:-1]
    return url


settings = get_settings()