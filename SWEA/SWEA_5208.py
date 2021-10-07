def dfs(n, c):
    global ans

    if c >= ans:
        return
    if n == N:
        ans = min(ans, c)
        return
        
    end = n+battery[n-1]
    if end > N:
        end = N
    for i in range(n+1, end+1):
        dfs(i, c+1)

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    N = nums[0]
    battery = nums[1:]
    ans = 100
    for i in range(2, battery[0]+2):
        dfs(i, 0)
    print('#{} {}'.format(tc, ans))