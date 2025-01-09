from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_health():
    response = client.get(url="/health")
    assert response.status_code == 200
    assert response.json() == "OK"


def test_get_hello_1():
    response = client.get(url="/everyone")
    assert response.status_code == 200
    assert response.json() == "Hello everyone"


def test_get_hello_2():
    response = client.get(url="/devops/engineers")
    assert response.status_code == 200
    assert response.json() == "Hello devops, engineers"


def test_get_hello_3():
    response = client.get(url="/devops/engineers/again")
    assert response.status_code == 200
    assert response.json() == "Hello devops, engineers, again"


# def test_get_hello_4():
#     response = client.get(url="/devops/engineers/once/more")
#     assert response.status_code == 200
#     assert response.json() == "Hello devops, engineers, once, more"


def test_not_found():
    response = client.get(url="/devops/engineers/again/and/again")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
