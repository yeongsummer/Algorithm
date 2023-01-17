def dfs(S, G):
    stack = []
    stack.append(S)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, V + 1):  # 인접 노드 순회
                if graph[v][w] == 1 and visited[w] == 0:
                    if w == G:
                        return 1
                    stack.append(w)
    return 0

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    visited = [0 for _ in range(V + 1)]
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1

    S, G = map(int, input().split())
    print('#{} {}'.format(tc+1, dfs(S, G)))