# 길찾기

from collections import defaultdict

def dfs(S):
    visited = []
    stack = [S]

    while stack:
        v = stack.pop()

        if v not in visited:
            visited.append(v)
            for w in G[v]:
                if w == 99:
                    return 1
                if w not in visited:
                    stack.append(w)
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = defaultdict(list)
    for i in range(0, len(temp)-1, 2):
        G[temp[i]] += [temp[i+1]]

    print('#{} {}'.format(tc, dfs(0)))
