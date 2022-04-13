import sys
from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    deq = deque([(x, y)])
    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                board[nx][ny] = 2
                deq.append((nx, ny))

def find(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2:
            cnt += 1

    if cnt >= 2:
        return True
    else:
        return False

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

bfs(0, 0)
for i in range(N):
    print(board[i])

time = -1
while True:
    time += 1
    remove_cheese = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                if find(i, j):
                    remove_cheese.append((i, j))

    if not remove_cheese:
        break

    for cheese in remove_cheese:
        x, y = cheese
        board[x][y] = 2

print(time)
