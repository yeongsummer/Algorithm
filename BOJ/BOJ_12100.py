from collections import deque

def move2(x, y, empty, temp, temp_x, temp_y):
    if board[x][y]:
        num = board[x][y]

        if temp == num:
            board[temp_x][temp_y] *=2
            board[x][y] = 0
            temp = 0
            temp_x, temp_y = -1, -1
            empty.append((x, y))
        else:
            if empty:
                empty_x, empty_y = empty.popleft()
                board[empty_x][empty_y] = num
                board[x][y] = 0
                temp_x, temp_y = empty_x, empty_y
                empty.append((x, y))
            else:
                temp_x, temp_y = x, y
            temp = num
    else:
        empty.append((x, y))
    return empty, temp, temp_x, temp_y

def move(d):

    if d == 0:
        for y in range(N):
            empty = deque()
            temp = 0
            temp_x, temp_y = -1, -1
            for x in range(N-1, -1, -1):
                empty, temp, temp_x, temp_y = move2(x, y, empty, temp, temp_x, temp_y)
    elif d == 1:
        for y in range(N):
            empty = deque()
            temp = 0
            temp_x, temp_y = -1, -1
            for x in range(N):
                empty, temp, temp_x, temp_y = move2(x, y, empty, temp, temp_x, temp_y)

    elif d == 2:
        for x in range(N):
            empty = deque()
            temp = 0
            temp_x, temp_y = -1, -1
            for y in range(N-1, -1, -1):
                empty, temp, temp_x, temp_y = move2(x, y, empty, temp, temp_x, temp_y)
    else:
        for x in range(N):
            empty = deque()
            temp = 0
            temp_x, temp_y = -1, -1
            for y in range(N):
                empty, temp, temp_x, temp_y = move2(x, y, empty, temp, temp_x, temp_y)
    

def easy(n, lst):
    global board, answer

    if n == 5:
        answer = max(answer, max(max(board[i]) for i in range(N)))
        return

    origin_board = [b[:] for b in board]

    for d in range(4):
        move(d)
        easy(n+1, lst+[d])
        board = [b[:] for b in origin_board]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
easy(0, [])
print(answer)
