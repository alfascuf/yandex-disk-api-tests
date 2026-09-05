import uuid

import pytest


@pytest.fixture
def temp_folder(disk_client):
    folder_name = f"test-folder-{uuid.uuid4()}"

    response = disk_client.create_folder(folder_name)
    assert response.status_code == 201

    yield folder_name

    disk_client.delete_resource(folder_name)


def test_create_folder(disk_client):
    folder_name = f"test-folder-{uuid.uuid4()}"

    response = disk_client.create_folder(folder_name)

    assert response.status_code == 201

    disk_client.delete_resource(folder_name)


def test_get_folder(disk_client, temp_folder):
    response = disk_client.get_resource(temp_folder)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == temp_folder
    assert data["type"] == "dir"


def test_delete_folder(disk_client):
    folder_name = f"delete-folder-{uuid.uuid4()}"

    create_response = disk_client.create_folder(folder_name)
    assert create_response.status_code == 201

    delete_response = disk_client.delete_resource(folder_name)

    assert delete_response.status_code in (202, 204)

    get_response = disk_client.get_resource(folder_name)

    assert get_response.status_code == 404


def test_copy_folder(disk_client, temp_folder):
    destination = f"copy-folder-{uuid.uuid4()}"

    copy_response = disk_client.copy_resource(
        temp_folder,
        destination,
    )

    assert copy_response.status_code in (201, 202)

    get_response = disk_client.get_resource(destination)

    assert get_response.status_code == 200

    disk_client.delete_resource(destination)


def test_get_nonexistent_resource(disk_client):
    path = f"missing-{uuid.uuid4()}"

    response = disk_client.get_resource(path)

    assert response.status_code == 404


def test_create_existing_folder(disk_client, temp_folder):
    response = disk_client.create_folder(temp_folder)

    assert response.status_code == 409