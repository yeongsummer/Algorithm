from collections import deque
def bfs(x, y):
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    deq = deque([(x,y)])

    while deq:
        x, y = deq.popleft()

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
    matrix = [list(map(int, list(input()))) for _ in range(100)]
    print('#{} {}'.format(tc, bfs(1,1)))