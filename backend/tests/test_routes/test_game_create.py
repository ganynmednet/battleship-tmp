import json


def test_create_user(client):
    data = {
        "player1": "Sergey",
        "player2": "Rossman",
        "board_size": 9,
        "num_turns": 50,
        "ships": {
            "battleship": True,
            "carrier": True,
            "destroyer": True
        }
    }
    response = client.post("/start/", json.dumps(data))

    print(response.json())
    assert response.status_code == 200
    assert response.json()["player1"] == "Sergey"
    assert response.json()["player2"] == "Rossman"
    assert response.json()["ended"] is False

    print("/game/{}/".format(response.json()["id"]))
    response = client.get("/game/{}/".format(response.json()["id"]))
    assert response.status_code == 200
    assert response.json()["player1"] == "Sergey"
    assert response.json()["player2"] == "Rossman"
    assert response.json()["ended"] is False
