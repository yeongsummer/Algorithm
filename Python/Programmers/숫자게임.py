def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_l, b_l = len(A), len(B)
    a = b = 0
    while a < a_l and b < b_l:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    
    return answer