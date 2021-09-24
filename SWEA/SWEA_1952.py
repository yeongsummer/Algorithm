# 수영장

T = int(input())
for tc in range(1, T+1):
    fees = list(map(int, input().split()))
    schedules = list(map(int, input().split()))

    dp = [0]*12
    dp[0] = min(fees[0]*schedules[0], fees[1])
    dp[1] = dp[0] + min(fees[0]*schedules[1], fees[1])

    for i in range(2, 12):
        dp[i] = min(dp[i-3]+fees[2], dp[i-1]+fees[0]*schedules[i], dp[i-1]+fees[1])

    ans = min(dp[11], fees[3])
    print('#{} {}'.format(tc, ans))