# 숫자 배열 회전
def rotate(N, matrix):
    result = [] # 90, 180, 270도 회전시킨 행렬을 저장할 리스트
    for i in range(3):
        matrix90 = [[0 for _ in range(N)] for _ in range(N)] # 현재 행렬을 90도 회전시킨 행렬을 저장할 변수

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
            print(*item[i], sep='', end=' ')
        print()

# 처음에 짰던 코드
T = int(input())

for test_case in range(1, T + 1):
    matrix = []
    N = int(input())
    result = []

    for _ in range(N):
        matrix.append(list(map(int,input().split())))

    for _ in range(3):
        trans_matrix = []
        for i in range(N):
            lst = []
            for j in range(N-1,-1,-1):
                lst.append(matrix[j][i])
            trans_matrix.append(lst)
        result.append(trans_matrix)
        matrix = trans_matrix
    
    print('#{}'.format(tc))
    for i in range(N):
        for item in result:
            print(*item[i], sep='', end=' ')
        print()