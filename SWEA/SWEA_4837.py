T = int(input())

A = [i+1 for i in range(12)]
for tc in range(T):
    N, S = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        if bin(i).count('1') != N: # 부분집합의 개수가 3이 아니면 아래 실행 X
            continue

        total = 0
        for j in range(12):
            if i & (1 << j):
                total += A[j]

        if total == S:
            cnt += 1

    print('#{0} {1}'.format(tc+1, cnt))