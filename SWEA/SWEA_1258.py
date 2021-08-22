T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                print(i,j)
                cnt += 1
                k = 1
                while j+k < N and matrix[i][j+k] != 0:
                    k += 1
                
                l = 1
                while i+l < N and matrix[i+l][j] != 0:
                    l += 1

                for r in range(i, i+l):
                    for c in range(j, j+k):
                        matrix[r][c] = 0
                result.append([l, k])

    result.sort(key = lambda x: (x[0]*x[1], x[0]))

    print('#{} {}'.format(tc, cnt), end=' ')
    for i in range(cnt):
        print(*result[i], end=' ')
    print()
