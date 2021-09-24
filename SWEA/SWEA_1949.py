# 등산로 조성
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(x, y, dist, K):
    global ans

    if dist > ans:
        ans = dist

    visited[x][y] = 1

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0:
            if mountain[nx][ny] < mountain[x][y]:
                dfs(nx, ny, dist+1, K)
            elif K and K > mountain[nx][ny] - mountain[x][y]:
                tmp = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1
                dfs(nx, ny, dist+1, 0)
                mountain[nx][ny] = tmp

    visited[x][y] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > top:
                top = mountain[i][j]

    ans = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                dfs(i, j, 1, K)

    print('#{} {}'.format(tc, ans))