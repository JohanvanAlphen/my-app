import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hallo wereld!"


def test_final(client):
    response = client.get("/final")

    assert response.status_code == 200
    assert response.data == b"My final assignment!!!"


def test_cow(client):
    response = client.get("/cow")

    assert response.status_code == 200
    assert response.data == b"MOoooOo!"
