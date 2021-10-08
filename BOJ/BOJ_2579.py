N = int(input())
stair = [0] + [int(input()) for _ in range(N)]
dp = [[0,0] for _ in range(N+1)]
dp[1][0] = dp[1][1] = stair[1]
for i in range(2, N+1):
    dp[i][0], dp[i][1] = stair[i] + dp[i-1][1], stair[i] + max(dp[i-2])
print(max(dp[N]))
