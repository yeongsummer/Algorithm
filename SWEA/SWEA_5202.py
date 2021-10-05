T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    time_list = sorted(time_list, key=lambda x: x[1])
    i = 0
    l = len(time_list)
    ans = 0
    end = 0
    while i < l:
        if time_list[i][0] >= end:
            ans += 1
            end = time_list[i][1]
        i += 1
    print('#{} {}'.format(tc, ans))