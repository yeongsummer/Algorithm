def dfs(n, items, total):
    global ans

    if total >= ans:
        return

    if n == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if i not in items:
            items.append(i)
            dfs(n+1, items, total+matrix[n][i])
            items.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 1500
    dfs(0, [], 0)
    print('#{} {}'.format(tc, ans))