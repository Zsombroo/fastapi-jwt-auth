import pytest
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(
    app,
    base_url="https://testserver.eu",
)


@pytest.fixture
def test_user_login_1():
    """ Happy path """
    response = client.post(
        url="/auth/login",
        data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "refresh_token" in response.cookies
    assert b"access_token" in response.content

    return response.cookies


def test_user_login_2():
    """ Incorrect creds """
    response = client.post(
        url="/auth/login",
        data={"username": "aoeu", "password": "snth"}
    )
    assert response.status_code == 401
    assert response.content == b'{"detail":"Invalid username or password"}'


def test_refresh_1():
    client.cookies = None
    response = client.post(
        url="/auth/refresh",
    )
    assert response.status_code == 401
    assert response.content == b'{"detail":"Refresh token not found"}'


def test_refresh_2(test_user_login_1):
    client.cookies = test_user_login_1
    response = client.post(
        url="/auth/refresh",
    )
    assert response.status_code == 200
    assert "refresh_token" in response.cookies
    assert b"access_token" in response.content


def test_protected_path(test_user_login_1):
    token = test_user_login_1.get("refresh_token")
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get(
        url="/user/profile",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.content == b'"Success"'


def test_protected_path():
    response = client.get(
        url="/user/profile",
    )
    assert response.status_code == 401
    assert response.content == b'{"detail":"Not authenticated"}'