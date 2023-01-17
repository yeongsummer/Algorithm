from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    room_list = [i for i in range(2, N+1)]
    ans = 9999999999
    for item in permutations(room_list, N-1):
        start = 1
        total = 0
        for end in item:
            total += matrix[start-1][end-1]
            start = end
        total += matrix[start-1][0]
        ans = min(ans, total)
    print('#{} {}'.format(tc, ans))