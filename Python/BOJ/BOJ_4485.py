from collections import deque
import sys

input = sys.stdin.readline
dxy = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    global visited
    deq = deque([(0, 0)])
    visited[0][0] = board[0][0]

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    deq.append((nx, ny))

idx = 1
while True:
    N = int(input().rstrip())
    if N == 0:
        break
    board = [list(map(int, input().rstrip().split())) for _ in range(N)]
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    bfs()
    print(f"Problem {idx}: {visited[N-1][N-1]}")
    idx += 1