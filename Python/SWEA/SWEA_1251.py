def find_MST(s):
    key[0] = 0

    for _ in range(N-1):
        min_idx = -1
        min_val = float('inf')
        for i in range(N):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        visited[min_idx] = 1

        for i in range(N):
            if adj_mat[min_idx][i] and not visited[i]:
                weight = adj_mat[min_idx][i]
                if weight < key[i]:
                    key[i] = weight

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node_x = list(map(int, input().split()))
    node_y = list(map(int, input().split()))
    E = float(input())

    adj_mat = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist = ((node_x[i]-node_x[j])**2+(node_y[i]-node_y[j])**2)*E
            adj_mat[i][j] = dist
            adj_mat[j][i] = dist

    key = [float('inf')]*N
    visited = [0]*N

    s = 0
    find_MST(s)
    print('#{} {}'.format(tc, round(sum(key))))