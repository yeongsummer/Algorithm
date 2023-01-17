from collections import deque

def dijkstra1(start):
    dp = [float('inf') for _ in range(N+1)]
    deq = deque([start])
    dp[start] = 0

    while deq:
        n = deq.popleft()
        for v in range(1, N+1):
            if matrix[v][n]:
                if dp[v] > dp[n] + matrix[v][n]:
                    dp[v] = dp[n] + matrix[v][n]
                    deq.append(v)
    return dp

def dijkstra2(start):
    dp = [float('inf') for _ in range(N+1)]
    deq = deque([start])
    dp[start] = 0

    while deq:
        n = deq.popleft()
        for v in range(1, N+1):
            if matrix[n][v]:
                if dp[v] > dp[n] + matrix[n][v]:
                    dp[v] = dp[n] + matrix[n][v]
                    deq.append(v)
    return dp

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        matrix[x][y] = c

    dp1 = dijkstra1(X)
    dp2 = dijkstra2(X)

    ans = 0
    for i, j in zip(dp1[1:], dp2[1:]):
        ans = max(ans, i+j)
    print('#{} {}'.format(tc, ans))