

def perform_shoot(board, shoot):
    if board[shoot[0]][shoot[1]] in [1, 3]:

        board[shoot[0]][shoot[1]] = 3

    else:
        board[shoot[0]][shoot[1]] = 2

    return board
