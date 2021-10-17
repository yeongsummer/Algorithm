# 미로
def bfs(x,y):
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    deq = [(x,y)]

    while deq:
        x, y = deq.pop(0)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if matrix[nx][ny] == 3:
                return 1

            if not matrix[nx][ny]:
                matrix[nx][ny] = 1
                deq.append((nx, ny))
    return 0

for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(16)]
    print('#{} {}'.format(tc, bfs(1,1)))

# 예전 코드

# def bfs(y, x):
#     q = [(y, x)]
#     dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위

#     while q:
#         y, x = q.pop(0)
#         if maze[y][x] == 0 or 2:
#             maze[y][x] = 1

#             for dy, dx in dxy:
#                 ny, nx = y + dy, x + dx

#                 if 0 <= ny <= 15 and 0 <= nx <= 15:
#                     if maze[ny][nx] == 0:
#                         q.append((ny, nx))
#                     elif maze[ny][nx] == 3:
#                         return 1
#     return 0

# for _ in range(10):
#     T = int(input())
#     maze = [list(map(int,list(input()))) for _ in range(16)]
#     for i in range(16):
#         if 2 in maze[i]:
#             sy, sx = i, maze[i].index(2)
#             break
#     print('#{} {}'.format(T, bfs(sy, sx)))
