import uuid
import pytest
import allure



@pytest.fixture
def temp_folder(disk_client):
    folder_name = f"test-folder-{uuid.uuid4()}"

    response = disk_client.create_folder(folder_name)
    assert response.status_code == 201

    yield folder_name

    disk_client.delete_resource(folder_name)


@allure.feature("Yandex Disk API")
@allure.story("Resources")
@allure.title("Create folder")
def test_create_folder(disk_client):
    folder_name = f"test-folder-{uuid.uuid4()}"

    with allure.step("Create folder"):
        response = disk_client.create_folder(folder_name)

    with allure.step("Check response status"):
        assert response.status_code == 201

    disk_client.delete_resource(folder_name)


@allure.feature("Yandex Disk API")
@allure.story("Resources")
@allure.title("Get folder information")
def test_get_folder(disk_client, temp_folder):
    with allure.step("Get folder information"):
        response = disk_client.get_resource(temp_folder)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == temp_folder
    assert data["type"] == "dir"


@allure.feature("Yandex Disk API")
@allure.story("Resources")
@allure.title("Delete folder")
def test_delete_folder(disk_client):
    folder_name = f"delete-folder-{uuid.uuid4()}"

    with allure.step("Create folder"):
        create_response = disk_client.create_folder(folder_name)
        assert create_response.status_code == 201

    with allure.step("Delete folder"):
        delete_response = disk_client.delete_resource(folder_name)
        assert delete_response.status_code in (202, 204)

    with allure.step("Check that folder no longer exists"):
        get_response = disk_client.get_resource(folder_name)
        assert get_response.status_code == 404


@allure.feature("Yandex Disk API")
@allure.story("Resources")
@allure.title("Copy folder")
def test_copy_folder(disk_client, temp_folder):
    destination = f"copy-folder-{uuid.uuid4()}"

    with allure.step("Copy folder"):
        copy_response = disk_client.copy_resource(
            temp_folder,
            destination,
        )

    assert copy_response.status_code in (201, 202)

    with allure.step("Check copied folder"):
        get_response = disk_client.get_resource(destination)
        assert get_response.status_code == 200

    disk_client.delete_resource(destination)


@allure.feature("Yandex Disk API")
@allure.story("Negative scenarios")
@allure.title("Get nonexistent resource")
def test_get_nonexistent_resource(disk_client):
    path = f"missing-{uuid.uuid4()}"

    response = disk_client.get_resource(path)

    assert response.status_code == 404


@allure.feature("Yandex Disk API")
@allure.story("Negative scenarios")
@allure.title("Create existing folder")
def test_create_existing_folder(disk_client, temp_folder):
    response = disk_client.create_folder(temp_folder)

    assert response.status_code == 409