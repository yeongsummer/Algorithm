T = int(input())
schedules = [list(map(int, input().split())) for _ in range(T)]
dp = [0 for _ in range(T)]
for i in range(T-1, -1, -1):
    if i == T-1:
        if schedules[i][0] == 1:
            dp[i] = schedules[i][1]
        else:
            dp[i] = 0
        continue
    if schedules[i][0] == 1:
        dp[i] = dp[i+1] + schedules[i][1]
    elif i + schedules[i][0]-1 < T:
        if i+schedules[i][0] > T-1:
            dp[i] = max(dp[i+1], 0 + schedules[i][1])
        else:
            dp[i] = max(dp[i+1], dp[i+schedules[i][0]] + schedules[i][1])
    else:
        dp[i] = dp[i+1]
print(dp[0])
