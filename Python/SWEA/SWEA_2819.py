dxy = [(1,0), (0,1), (-1,0), (0,-1)]
def dfs(x, y, num, c):
    if c == 7:
        if num not in answers:
            answers.add(num)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if -1 < nx < 4 and -1 < ny < 4:
            dfs(nx, ny, num + matrix[nx][ny], c+1)

T = int(input())
for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    answers = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, matrix[i][j], 1)

    print('#{} {}'.format(tc, len(answers)))
