def rotate(n, matrix):
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[j][n-i-1]
    return new_matrix

def solution(key, lock):
    answer = True
    
    return answer