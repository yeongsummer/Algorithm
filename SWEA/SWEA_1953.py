# 탈주범 검거
from collections import deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]

def bfs(r, c):
    global ans
    deq = deque()
    deq.append((r, c))
    time[r][c] = 1

    while deq:
        x, y = deq.popleft()
        ans += 1
        if time[x][y] >= L:
            continue

        for d in range(4):
            if pipe[hole[x][y]][d] == 0:
                continue

            nx, ny = x + dxy[d][0], y + dxy[d][1]
            nd = (d + 2) % 4
            if -1 < nx < N and -1 < ny < M and pipe[hole[nx][ny]][nd] and time[nx][ny] == 0:
                time[nx][ny] = time[x][y] + 1
                deq.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    hole = [list(map(int, input().split())) for _ in range(N)]
    time = [[0 for _ in range(M)] for _ in range(N)]
    ans = 0
    bfs(R, C)
    print('#{} {}'.format(tc, ans))