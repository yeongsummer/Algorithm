T = int(input())
for tc in range(T):
    N = int(input())

    matrix = [[0]*N for i in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1
    i, j = 0, -1
    k = 0
    while cnt <= N*N:
        x, y = i+dx[k], j+dy[k]
        if x < N and y < N and matrix[x][y] == 0:
            matrix[x][y] = cnt
            cnt += 1
            i, j = x, y
        else:
            k = (k+1) % 4

    print('#{0}'.format(tc+1))
    for i in matrix:
        print(*i)