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

## Run tests

- pytest -v

для Allure-результатов:
- pytest -v --alluredir=allure-results

Для просмотра отчета:
- allure serve allure-results

## Environment

- set YANDEX_DISK_TOKEN=your_token
