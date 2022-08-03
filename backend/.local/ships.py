import numpy
import random


def print_board(board):
    print("\n")
    for i in board:
        print(" ".join(map(str, i)))

    # print(board)
    # print(numpy.array(board).transpose())


if __name__ == "__main__":
    """
    generate ships
    find location
    place
    
    """

    board = [[0] * 10 for _ in range(10)]
    ships = [3, 3]


    # print_board(board)

    def place_ship(board, ships):

        def place(board, ship, orientation):
            """
            issue with located close to each other
            """

            location = (random.randint(0, 10 - ship), random.randint(0, 10 - ship))

            if orientation == 1:
                for i in range(ship):

                    if board[location[0]][location[1] + i] != 0:
                        return place(board, ship, orientation)

                    board[location[0]][location[1] + i] = 99
            else:
                for i in range(ship):

                    if board[location[0] + i][location[1]] != 0:
                        return place(board, ship, orientation)

                    board[location[0] + i][location[1]] = 99

            print("PLACEMENT IS DONE!")
            return board

        for ship in ships:
            orientation = random.randint(0, 1)  # 1 hor, 0 vert
            # orientation = 0
            print(ship)

            b = place(board, ship, orientation)
            print_board(b)

            # if orientation == 1:
            #     b = place(board, ship, orientation)
            #     print_board(b)
            # else:
            #
            #     board[1][2] = 5
            #     # print(board[2][1])
            #     # print(board[5])
            #     # print(board[3])
            #
            #     # b = place_h(board, ship, orientation)
            #     print_board(board)


    place_ship(board, ships)
