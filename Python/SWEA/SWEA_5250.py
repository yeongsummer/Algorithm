from collections import deque

def dijkstra(x,y):
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    deq = deque([(x, y)])
    dp[x][y] = 0

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < N:
                diff = 0
                if matrix[nx][ny] > matrix[x][y]:
                    diff += matrix[nx][ny] - matrix[x][y]

                if dp[nx][ny] > dp[x][y] + diff + 1:
                    deq.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + diff + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    ans = float('inf')
    dijkstra(0,0)
    print('#{} {}'.format(tc, dp[N-1][N-1]))