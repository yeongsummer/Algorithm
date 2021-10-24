dx = [1,0,-1,0]
dy = [0,1,0,-1]

def move(x, y, i, n):
    x += dx[i]
    y += dy[i]
    if x < n or x >= N-n or y < n or y >= M-n:
        x -= dx[i]
        y -= dy[i]
        i = (i+1)%4
        x += dx[i]
        y += dy[i]        
    return x, y, i

def rotate(matrix):
    for n in range(min(N, M)//2):
        x = y = n
        nx = ny = n
        i = ni = 0
        for _ in range(R):
            nx, ny, ni = move(nx, ny, ni, n)

        new_matrix[nx][ny] = matrix[x][y]

        while True:
            x, y, i = move(x, y, i, n)
            nx, ny, ni = move(nx, ny, ni, n)
            if x == y == n:
                break
            new_matrix[nx][ny] = matrix[x][y]
        
N, M, R = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
new_matrix = [[0 for _ in range(M)] for _ in range(N)]
rotate(matrix)
for i in range(N):
    print(*new_matrix[i])

