def bfs(y, x):
    distance = [[0 for _ in range(N)] for _ in range(N)]
    q = [(y, x)]

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    while q:
        y, x = q.pop(0)
        if maze[y][x] == 0 or 2:
            maze[y][x] = 1

            for dy, dx in dxy:
                ny, nx = y + dy, x + dx

                if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                    if maze[ny][nx] == 0:
                        distance[ny][nx] = distance[y][x] + 1
                        q.append((ny, nx))
                    elif maze[ny][nx] == 3:
                        return distance[y][x]
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sy, sx = i, maze[i].index(2)
            break
    print('#{} {}'.format(tc, bfs(sy, sx)))