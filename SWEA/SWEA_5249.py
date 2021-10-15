def find_MST(s):
    key[0] = 0

    for _ in range(V):
        min_idx = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        visited[min_idx] = 1

        for i in range(V+1):
            if adj_mat[min_idx][i] and not visited[i]:
                weight = adj_mat[min_idx][i]
                if weight < key[i]:
                    key[i] = weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for n1, n2, w in edges:
        adj_mat[n1][n2] = w
        adj_mat[n2][n1] = w


    key = [float('inf')] * (V+1)
    visited = [0] * (V+1)

    s = 0
    find_MST(s)

    print('#{} {}'.format(tc, sum(key)))