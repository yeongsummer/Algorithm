# 수열

N, K = map(int, input().split())
temperature = list(map(int, input().split()))
s = max_sum = sum(temperature[:K])
for i in range(K, N):
    s -= temperature[i-K]
    s += temperature[i]
    if s > max_sum:
        max_sum = s
print(max_sum)