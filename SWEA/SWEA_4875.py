def dfs(sy, sx):
    stack = [(sy, sx)]

    dyx = ((0, 1), (-1, 0), (1, 0), (0, -1))
    while stack:
        y, x = stack.pop()
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] == 0:
                    stack.append((ny, nx))
                elif maze[ny][nx] == 3:
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, str(input()))) for _ in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sy, sx = i, maze[i].index(2)
            break
    print('#{} {}'.format(tc, dfs(sy, sx)))
