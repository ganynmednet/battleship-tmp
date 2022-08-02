import json


def test_create_user(client):
    data = {
        "name_player1": "Sergey",
        "name_player2": "Rossman",
        "num_rounds": 10,
        "ships": {
            "carrier": True,
            "battleship": True,
            "destroyer": True,
            "cruiser": True
        }
    }
    response = client.post("/start/", json.dumps(data))

    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["name_player1"] == "Sergey"
    assert response.json()["name_player2"] == "Rossman"
    assert response.json()["ended"] is False

    # print("/game/{}/".format(response.json()["id"]))

    response = client.get("/game/{}/".format(response.json()["id"]))
    print(json.dumps(response.json()))
    assert response.status_code == 200
    assert response.json()["name_player1"] == "Sergey"
    assert response.json()["name_player2"] == "Rossman"
    assert response.json()["ended"] is False
