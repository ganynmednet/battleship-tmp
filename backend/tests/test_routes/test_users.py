import json


def test_users(client):
    data = {
        "username": "testuser",
        "password": "testing"
    }
    response = client.post("/users/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["is_active"] == True

    # check invalid password
    # data = {
    #     "username": "testuser@nofoobar.com",
    #     "password": "testing"
    # }
    #
    # response = client.post("/login/", json.dumps(data))
    # print(json.dumps(response.json()))
    # assert response.status_code == 401
    # assert response.json()["detail"] == "Incorrect username or password"

    # check valid password
    data = {
        "username": "testuser",
        "password": "testing"
    }

    response = client.post("/login/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"


