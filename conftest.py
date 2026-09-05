import os

import pytest

from api.disk_client import YandexDiskClient


@pytest.fixture(scope="session")
def disk_client():
    token = os.getenv("YANDEX_DISK_TOKEN")

    if not token:
        pytest.fail("YANDEX_DISK_TOKEN is not set")

    return YandexDiskClient(token)