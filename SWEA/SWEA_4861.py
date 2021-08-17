def trans_matrix(A): # 전치행렬 구하는 함수
    row = len(A)
    col = len(A[0])

    B = [[0 for row in range(row)] for col in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i] = A[i][j]
    return B

def palindrome(text): # 회문인지 판별하는 함수
    start = 1
    end = len(text)-2
    while start <= end:
        if text[start] == text[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def func(matrix, N, M):

    #가로로 찾기
    for lst in matrix:
        start = 0
        while start + M <= N:
            if lst[start] == lst[start + M - 1]:
                text = lst[start:start + M]
                if palindrome(text):
                    return text
            start += 1
    
    # 세로로 찾기
    matrix_T = trans_matrix(matrix)
    for lst in matrix_T:
        start = 0
        while start + M <= N:
            if lst[start] == lst[start + M - 1]:
                text = lst[start:start + M]
                if palindrome(text):
                    return text
            start += 1
    return 0 # 못 찾았을 경우

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    print('#{0}'.format(tc+1), ''.join(func(matrix, N, M)))