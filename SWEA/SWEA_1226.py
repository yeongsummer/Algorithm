# 미로

def bfs(y, x):
    q = [(y, x)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위

    while q:
        y, x = q.pop(0)
        if maze[y][x] == 0 or 2:
            maze[y][x] = 1

            for dy, dx in dxy:
                ny, nx = y + dy, x + dx

                if 0 <= ny <= 15 and 0 <= nx <= 15:
                    if maze[ny][nx] == 0:
                        q.append((ny, nx))
                    elif maze[ny][nx] == 3:
                        return 1
    return 0

for _ in range(10):
    T = int(input())
    maze = [list(map(int,list(input()))) for _ in range(16)]
    for i in range(16):
        if 2 in maze[i]:
            sy, sx = i, maze[i].index(2)
            break
    print('#{} {}'.format(T, bfs(sy, sx)))
