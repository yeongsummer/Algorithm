from collections import deque

def bfs(x, y, l):
    global max_len

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    deq = deque()
    deq.append((x, y, l))
    visited[x][y] = 1

    while deq:
        x, y, l = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < N:
                if matrix[nx][ny] == matrix[x][y] + 1:
                    deq.append((nx, ny, l+1))
                    visited[x][y] = 1

    if l > max_len:
        max_len = l

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                max_len = 0
                bfs(i, j, 1)
                if max_len > ans:
                    ans = max_len
                    n = matrix[i][j]
                elif max_len == ans and matrix[i][j] < n:
                    n = matrix[i][j]
    print('#{} {} {}'.format(tc, n, ans))