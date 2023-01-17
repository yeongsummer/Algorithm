# 진기의 최고급 붕어빵

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = deque(sorted(list(map(int, input().split()))))

    i = 0
    cnt = 0
    result = "Possible"
    while people:
        t = people.popleft()
        cnt = t // M * K - i
        if cnt - 1 < 0:
            result = "Impossible"
            break
        i += 1
    print("#{} {}".format(tc, result))

