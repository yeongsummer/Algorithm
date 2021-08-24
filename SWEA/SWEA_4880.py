def rsp(a, b):
    RSP = {1: (3, 2), 2: (1, 3), 3: (2, 1)}
    if numbers[a] == numbers[b]:
        return a
    elif RSP[numbers[a]][0] == numbers[b]:
        return a
    elif RSP[numbers[a]][1] == numbers[b]:
        return b

def tournament(start, end):
    if start == end:
        return start

    left = tournament(start, (start + end)//2)
    right = tournament((start + end)//2 + 1, end)

    return rsp(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(0, N-1)+1))