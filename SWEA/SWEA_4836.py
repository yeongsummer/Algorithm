T = int(input())

for tc in range(T):
    matrix = [[0]*10 for _ in range(10)]

    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        if color == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    matrix[i][j] += 1
        else:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    matrix[i][j] += 1

        cnt = 0
        for i in range(10):
            for j in range(10):
                if matrix[i][j] == 2:
                    cnt += 1

    print('#{0} {1}'.format(tc+1, cnt))