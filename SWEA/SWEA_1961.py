# 숫자 배열 회전
def rotate(N, matrix):
    result = []
    for i in range(3):
        matrix90 = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                matrix90[j][N-1-i] = matrix[i][j]
        result.append(matrix90)
        matrix = matrix90
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = rotate(N, matrix)
    print('#{}'.format(tc))
    for i in range(N):
        for item in result:
            print(*item[i],sep='',end=' ')
        print()

