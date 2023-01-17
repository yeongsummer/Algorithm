def concert(K,N,M):
    if K > N*M:
        return [0]

    matrix = [[0 for _ in range(N)] for i in range(M)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 1
    i, j = M, 0
    k = 0
    while cnt <= N*M:
        x, y = i+dx[k], j+dy[k]
        if -1 < x < M and -1 < y < N and matrix[x][y] == 0:
            if cnt == K:
                return [y+1, M-x]

            matrix[x][y] = cnt
            cnt += 1
            i, j = x, y
        else:
            k = (k+1) % 4

N, M = map(int, input().split())
K = int(input())
print(*concert(K,N,M))

