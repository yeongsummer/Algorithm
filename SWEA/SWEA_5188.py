dxy = [(0,1),(1,0)]
def dfs(x, y, s):
    global ans

    if s >= ans:  # 가지치기
        return

    if x == N-1 and y == N-1:  # 도착지에 도착한 경우
        if s < ans:
            ans = s
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx > -1 and nx < N and ny > -1 and ny < N:
            dfs(nx, ny, s+matrix[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999
    dfs(0, 0, matrix[0][0])
    print('#{} {}'.format(tc, ans))
