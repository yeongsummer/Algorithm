from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    talls = list(map(int, input().split()))
    talls.sort()
    n = 0
    ans = float('inf')
    while n <= N:
        n += 1
        if sum(talls[N-n:]) < B:
            continue
        for item in combinations(talls, n):
            s = sum(item)
            if s >= B and s < ans:
                ans = s
    print('#{} {}'.format(tc, ans-B))
