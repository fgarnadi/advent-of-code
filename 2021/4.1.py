from sys import stdin

board_size = 5

def mark(board, x):
    _sum = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == x:
                board[i][j] *= -1

    return board

def check_win(board):
    # horizontal
    for i in range(board_size):
        marked = sum(map(int, [x < 0 for x in board[i]]))
        if marked == board_size:
            return True

    # vertical
    for i in range(board_size):
        marked = sum(map(int, [x[i] < 0 for x in board]))
        if marked == board_size:
            return True

    # diagonal
    d1 = sum(map(int, [board[i][i] < 0 for i in range(board_size)]))
    if d1 == board_size:
        return True

    d2 = sum(map(int, [board[i][i] < 0 for i in range(board_size-1, -1, -1)]))
    if d2 == board_size:
        return True

    return False

def count_score(board):
    _sum = 0
    for i in range(board_size):
        _sum += sum(filter(lambda x: x > 0, board[i]))

    return _sum

if __name__ == '__main__':
    command = input()
    command = list(map(int, command.split(',')))

    i = -1
    _board = []
    for line in stdin:
        line = line.strip()
        if (line == ''):
            _board.append([])
            i += 1
            continue
        
        _board[i].append(list(map(int, line.split())))

    for cmd in command:
        for board in _board:
            board = mark(board, cmd)

            if(check_win(board)):
                print(count_score(board) * cmd)
                exit()