K,N = map(int,input().split())
line = []

for _ in range(K):
    line.append(int(input())) 
start, end = 1, max(line)

while start <= end:
    mid = (start + end) // 2 
    n = 0
    for i in line:
        n += i // mid  
    if n >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)