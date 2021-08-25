# 색종이
matrix = [[0 for _ in range(1001)] for _ in range(1001)]
N = int(input())
for n in range(1, N+1):
    y, x, w, h = map(int, input().split())

    for i in range(h):
        for j in range(w):
            matrix[1000-x-i][y+j] = n

for n in range(1, N+1):
    cnt = 0
    for i in range(1001):
        cnt += matrix[i].count(n)
    print(cnt)