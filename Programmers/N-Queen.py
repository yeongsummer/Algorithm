def is_available(queens, c, r):
    for i in range(len(queens)):
        if queens[i] == c or abs(queens[i] - i) == abs(r - c):
            return False
    return True


def dfs(answer, N, r, queens):
    if r == N:
        answer += 1
        return
    
    for c in range(N):
        if is_available(queens, c, r):
            queens.append(c)
            dfs(answer, N, r+1, queens)
            queens.pop()

    
def solution(n):
    answer = 0

    def is_available(queens, c, r):
        for i in range(len(queens)):
            if queens[i] == c or abs(queens[i] - c) == abs(r - i):
                return False
        return True


    def dfs(N, r, queens):
        nonlocal answer

        if r == N:
            answer += 1
            return
        
        for c in range(N):
            if is_available(queens, c, r):
                queens.append(c)
                dfs(N, r+1, queens)
                queens.pop()


    dfs(n, 0, [])
    return answer

print(solution(4))