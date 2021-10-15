def dfs(s, n):
    global ans
    if n > ans:
        ans = n

    for v in node[s]:
        if not visited[v]:
            visited[v] = 1
            dfs(v, n+1)
            visited[v] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    node = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        node[n1].append(n2)
        node[n2].append(n1)

    ans = 0
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print('#{} {}'.format(tc, ans))