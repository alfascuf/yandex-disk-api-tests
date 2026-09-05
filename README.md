# Yandex Disk API Tests

Пример проекта автотестов для REST API Яндекс.Диска.

## Stack

- Python 3
- Pytest
- Requests

## Covered methods

- GET — получение информации о ресурсе
- PUT — создание папки
- POST — копирование ресурса
- DELETE — удаление ресурса

Также добавлены негативные сценарии:

- получение несуществующего ресурса
- повторное создание существующей папки

## Project structure

```text
api/
    disk_client.py
tests/
    test_disk_api.py
conftest.py
pytest.ini
requirements.txt