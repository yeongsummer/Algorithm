N = 123456*2 +1
lst = [1] * N
for i in range(2, int(N**0.5)+1):
    for j in range(2*i, N, i):
        lst[j] = 0
    
while True:
    n = int(input())
    if not n:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if lst[i]:
            cnt += 1
    print(cnt)

