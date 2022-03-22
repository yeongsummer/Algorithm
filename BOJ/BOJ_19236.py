from copy import deepcopy
def dfs(x, y, total, n):
    global board, answer

    print(x, y, total, n)

    for i in range(4):
        print(board[i])

    if n > 3:
        return

    answer = max(answer, total)

    for i in range(16):
        if locations[i] == 0:
            continue

        f_x, f_y = locations[i]
        origin_d = board[f_x][f_y][1]
        d = origin_d

        while True:
            f_nx, f_ny = f_x + dxy[d][0], f_y + dxy[d][1]

            if 0 <= f_nx < 4 and 0 <= f_ny < 4 and board[f_nx][f_ny][0]:
                locations[i] = (f_nx, f_ny)
                locations[board[f_nx][f_ny][0]-1] = (f_x, f_y)
                board[f_x][f_y] = board[f_nx][f_ny]
                board[f_nx][f_ny] = [i+1, d]
                break
            
            d = (d+1) % 8

            if d == origin_d:
                break
    
    s_d = board[x][y][1]
    nx, ny = x + dxy[s_d][0], y + dxy[s_d][1]

    print('shark:', s_d, x, y)
    origin_board = deepcopy(board)
    while 0 <= nx < 4 and 0 <= ny < 4:
        if board[nx][ny][0]:
            fish = board[nx][ny][0]
            board[nx][ny][0] = 0
            location = locations[fish-1]
            locations[fish-1] = 0
            dfs(nx, ny, total+fish, n+1)
            board = origin_board
            board[nx][ny][0] = fish
            locations[fish-1] = location

        print(nx, ny)
        nx, ny = nx + dxy[s_d][0], ny + dxy[s_d][1]



dxy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
locations = [0]*16
board = [[0]*4 for _ in range(4)]
for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        board[i][j//2] = [inp[j], inp[j+1]-1]
        locations[inp[j]-1] = (i, j//2)
answer = 0
start = board[0][0][0]
locations[start-1] = 0
board[0][0][0] = 0
dfs(0, 0, start, 0)

print(board)
print(locations)