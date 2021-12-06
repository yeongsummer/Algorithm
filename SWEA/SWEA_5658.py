T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())
    R = N//4
    i = 0
    result_list = set()
    while i < R:
        for idx in range(0, N-R+1, R):
            result = int(''.join(numbers[idx:idx+R]),16)
            result_list.add(result)
        numbers.append(numbers.pop(0))

        i += 1
    result_list = sorted(list(result_list), reverse = True)
    print('#{} {}'.format(tc, result_list[K-1]))