from collections import deque
import sys

input = sys.stdin.readline

dxy = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():
    global visited

    deq = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while deq:
        x, y, c = deq.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][c]

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny]:
                    if not c:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        deq.append((nx, ny, 1))
                else:
                    if not visited[nx][ny][c]:
                        visited[nx][ny][c] = visited[x][y][c] + 1
                        deq.append((nx, ny, c))
                    else:
                        if visited[x][y][c] + 1 < visited[nx][ny][c]:
                            visited[nx][ny][c] = visited[x][y][c] + 1
                            deq.append((nx, ny, c))
    return -1

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]

print(bfs())
