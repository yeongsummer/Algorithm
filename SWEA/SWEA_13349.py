dxy = [(-1,0), (0,1), (1,0), (0,-1)]
def dfs(x, y, l, c):
    global min_cnt
    stack = [(x,y,l,c,[(x,y)])]
    while stack:
        x, y, l, c, visited = stack.pop(0)
        if c >= min_cnt:
            continue

        if x == start_x and y == start_y:
            min_cnt  = min(min_cnt, c)
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if -1 < nx < M and -1 < ny < N and (nx, ny) not in visited:
                # print(nx, ny, l-1, c)
                if l >= 1:
                    if matrix[nx][ny] == 1:
                        stack.append((nx, ny, L, c+1, visited+[(nx, ny)]))
                    else:
                        stack.append((nx, ny, l-1, c, visited+[(nx, ny)]))
    
T = int(input())
for tc in range(1, T+1):
    M, N, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 2:
                start_x, start_y = i, j
            elif matrix[i][j] == 3:
                end_x, end_y = i, j
    
    min_cnt = M*N
    dfs(end_x, end_y, L, 0)

    if min_cnt == M*N:
        result = -1
    else:
        result = min_cnt
    print('#{} {}'.format(tc, result))
