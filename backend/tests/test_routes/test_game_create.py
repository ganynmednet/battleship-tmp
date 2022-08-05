import json
from tests.conftest import Players

players = Players()


# def test_create_player1(client):
#     print("\nCREATE PLAYER 1 >>>")
#     data = {
#         "username": "Player1",
#         "password": "testing",
#         "name": "Sergey Player1"
#     }
#     response = client.post("/users/", json.dumps(data))
#     print(json.dumps(response.json()))
#     assert response.status_code == 200
#     assert response.json()["username"] == "Player1"
#     assert response.json()["is_active"] == True
#
#     data = {
#         "username": "Player1",
#         "password": "testing",
#     }
#
#     response = client.post("/login/", json.dumps(data))
#     print(json.dumps(response.json()))
#     assert response.status_code == 200
#     assert response.json()["access_token"]
#     assert response.json()["token_type"] == "bearer"
#
#     players.player1_id = response.json()["user_id"]
#
#
# def test_create_player2(client):
#     print("\nCREATE PLAYER 1 >>>")
#     data = {
#         "username": "Player2",
#         "password": "testing",
#         "name": "Rossman Player2"
#     }
#     response = client.post("/users/", json.dumps(data))
#     print(json.dumps(response.json()))
#     assert response.status_code == 200
#     assert response.json()["username"] == "Player2"
#     assert response.json()["is_active"] == True
#
#     data = {
#         "username": "Player2",
#         "password": "testing"
#     }
#
#     response = client.post("/login/", json.dumps(data))
#     print(json.dumps(response.json()))
#     assert response.status_code == 200
#     assert response.json()["access_token"]
#     assert response.json()["token_type"] == "bearer"
#
#     players.player2_id = response.json()["user_id"]


def test_create_game(client):
    print("\nCREATE PLAYER 1 >>>")
    data = {
        "username": "Player1",
        "password": "testing",
        "name": "Sergey Player1"
    }
    response = client.post("/users/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["username"] == "Player1"
    assert response.json()["is_active"] == True

    data = {
        "username": "Player1",
        "password": "testing",
    }

    response = client.post("/login/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"
    Players.player1_token = response.json()["access_token"]
    players.player1_id = response.json()["user_id"]

    print("\nCREATE PLAYER 1 >>>")
    data = {
        "username": "Player2",
        "password": "testing",
        "name": "Rossman Player2"
    }
    response = client.post("/users/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["username"] == "Player2"
    assert response.json()["is_active"] == True

    data = {
        "username": "Player2",
        "password": "testing"
    }

    response = client.post("/login/", json.dumps(data))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"] == "bearer"
    Players.player2_token = response.json()["access_token"]
    players.player2_id = response.json()["user_id"]

    print("\nCREATE GAME >>>")
    # print("TEST RESULTS")
    print(players.player1_id, players.player2_id)

    data = {
        "player1_id": players.player1_id,
        "player2_id": players.player2_id,
        "num_rounds": 10,
        "ships": {
            "carrier": True,
            "battleship": True,
            "destroyer": True,
            "cruiser": True
        }
    }
    response = client.post("/start/", json.dumps(data))

    print("\n", json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["player1"]["name"] == "Sergey Player1"
    assert response.json()["player2"]["name"] == "Rossman Player2"
    assert response.json()["ended"] is False

    Players.game_id = response.json()["id"]

    data = {
        "game_id": Players.game_id,
        "hor": 1,
        "ver": 1
    }

    headers = {
        "authorization": "Bearer {}".format(Players.player1_token)
    }

    response = client.get("/shoot/{}/{}/{}".format(
        data["game_id"],
        data["hor"],
        data["ver"]),
        headers=headers
    )
    print("\n", json.dumps(response.json()))

#
#     # print("/game/{}/".format(response.json()["id"]))
#
#     response = client.get("/game/{}/".format(response.json()["id"]))
#     print(json.dumps(response.json()))
#     assert response.status_code == 200
#     assert response.json()["name_player1"] == "Sergey"
#     assert response.json()["name_player2"] == "Rossman"
#     assert response.json()["ended"] is False
