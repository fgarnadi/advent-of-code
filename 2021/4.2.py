from sys import stdin
from functools import reduce

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

    board_len = -1
    boards = []
    for line in stdin:
        line = line.strip()
        if (line == ''):
            boards.append([[], False])
            board_len += 1
            continue
        
        boards[board_len][0].append(list(map(int, line.split())))

    win_count = 0
    for cmd in command:
        for board in boards:
            if board[1]:
                continue

            board[0] = mark(board[0], cmd)

            if(check_win(board[0])):
                win_count += 1
                board[1] = True
                if win_count == board_len+1:
                    print(count_score(board[0]) * cmd)
                    exit()