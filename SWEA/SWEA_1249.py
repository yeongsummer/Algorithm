from collections import deque

def dijkstra(x,y):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    deq = deque([(x, y)])
    dp[x][y] = 0

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < N:
                if dp[nx][ny] > dp[x][y] + matrix[nx][ny]:
                    deq.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + matrix[nx][ny]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    dijkstra(0,0)
    print('#{} {}'.format(tc, dp[N-1][N-1]))