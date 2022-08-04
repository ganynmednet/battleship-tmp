import numpy
import random


def print_board(board):
    print("\n")
    for i in board:
        print(" ".join(map(str, i)))


if __name__ == "__main__":

    ships = {
        "carrier": True,
        "battleship": True,
        "cruiser": True,
        "destroyer": True
    }


    def generate_board(ships):
        board = [[0] * 10 for _ in range(10)]

        SHIP_CONFIG = dict(
            carrier=dict(
                num=1,
                length=5
            ),
            battleship=dict(
                num=2,
                length=4
            ),
            cruiser=dict(
                num=3,
                length=3
            ),
            destroyer=dict(
                num=4,
                length=2
            )
        )

        def deploy_ship(board, ship, orientation):
            print("SHIP DEPLOYMENT")
            locations = []

            if orientation == 0:
                for r in range(len(board)):
                    for x in range(len(board[r]) - ship):
                        if 1 not in board[r][x - 1:x + ship + 1]:
                            # if r < len(board):
                            #     if 1 not in board[r + 1][x - 1:x + ship + 1]:
                            locations.append((r, x))

                location = random.choice(locations)
                for i in range(ship):
                    board[location[0]][location[1] + i] = 1

            else:
                for r in range(len(board[0]) - ship):
                    # print(board[r])
                    for x in range(len(board)):
                        if 1 not in [board[r - 1 + i + 1][x] for i in range(ship)]:
                            locations.append((r, x))

                location = random.choice(locations)
                for i in range(ship):
                    board[location[0] + i][location[1]] = 1

            return locations

        for ship_type in ships:
            print("\nSHIP TYPE >>>>>>> ", ship_type)
            if ship_type:

                if ship_type in ["carrier", "battleship", "cruiser", "destroyer"]:

                    for i in range(1, SHIP_CONFIG[ship_type]["num"] + 1):
                        # if i < 2:
                        ship = SHIP_CONFIG[ship_type]["length"]
                        orientation = random.randint(0, 1)  # 0 hor, 1 vert

                        deploy_ship(board, ship, orientation)

                        print_board(board)

        return board


    def shooter(board, shoot):

        if board[shoot[0]][shoot[1]] in [1, 3]:

            board[shoot[0]][shoot[1]] = 3

        else:
            board[shoot[0]][shoot[1]] = 2

        print_board(board)


    b = generate_board(ships)

    print("all ready")
    print_board(b)

    shooter(b, (1, 1))
