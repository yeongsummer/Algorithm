T = int(input())

for test_case in range(1, T + 1):
    length = int(input())
    cost_list = list(map(int,input().split()))
    cost = cost_list[-1]
    result = 0
    for i in range(length-2,-1,-1):
        if cost_list[i] > cost :
            cost = cost_list[i]
        else:
            result += cost - cost_list[i]
    print(f'#{test_case} {result}')