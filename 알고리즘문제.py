def bfs():
    q = []
    visited[0][0][0] = 1
    q.append((0, 0, False))
    while q:
        x, y, shoes = q.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1:
                if arr[x][y] == 2:  # 운동화를 처음 만났을 때
                    q.append((nx, ny, True))
                    visited[nx][ny][1] = visited[x][y][0] + 1
                else:
                    if shoes:  # 운동화를 신은 상태라면
                        if visited[nx][ny][1] == 0:
                            q.append((nx, ny, shoes))
                            visited[nx][ny][1] = visited[x][y][1] + 1
                    else:  # 운동화를 신은 상태가 아니라면
                        if visited[nx][ny][0] == 0:
                            q.append((nx, ny, shoes))
                        visited[nx][ny][0] = visited[x][y][0] + 2

dx = [0,1,0,-1]
dy = [1,0,-1,0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
bfs()
for i in range(n):
    print(visited[i])
print(min(visited[n-1][m-1]))