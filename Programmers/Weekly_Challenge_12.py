from itertools import permutations

def solution(k, dungeons):
    def game(n, lst, p):
        nonlocal ans
        if n > ans:
            ans = n
        if n == C:
            return
        if p >= lst[n][0]:
            game(n+1, lst, p - lst[n][1])
            
    ans = 0  
    C = len(dungeons)
    for lst in permutations(dungeons, C):
        print(lst)
        game(0, lst, k)

    return ans

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))