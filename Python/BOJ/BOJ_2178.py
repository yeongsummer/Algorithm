from collections import deque

def bfs(maze, start_y, start_x):
    distance = [[0 for _ in range(M)] for _ in range(N)]
    q = [(start_y, start_x)]
    distance[start_y][start_x] = 1

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    while q:
        y, x = q.pop(0)

        if y == N-1 and x == M-1 :
            print(distance)
            return distance[y][x]

        for dy, dx in dxy:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1 and not distance[ny][nx]:
                distance[ny][nx] = distance[y][x] + 1
                q.append((ny, nx))

    return distance[y][x]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
print(bfs(maze, 0, 0))