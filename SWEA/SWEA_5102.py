def bfs(S, G):
    q = [S]
    visited[S] = 1
    while q:
        v = q.pop(0)
        for i in g[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

            if i == G:
                return visited[i] - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    S, G = map(int, input().split())
    answer = bfs(S, G)
    print('#{} {}'.format(tc, answer))