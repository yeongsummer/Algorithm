N = int(input())
K = int(input())

for _ in range(K):
    a, b = map(int, input().split())
    h = N // 2
    if a > h:
        a = N + 1 - a
    if b > h:
        b = N + 1 - b
    if b // a == 0:
        c = b % 3
    else:
        c = a % 3
    if c == 0:
        c = 3
    print(c)