# 색종이
matrix = [[0 for _ in range(1001)] for _ in range(1001)]
N = int(input())
for n in range(1, N+1):
    y, x, w, h = map(int, input().split())

    for i in range(h):
        matrix[1000-x-i][y:y+w] = [n]*w

for n in range(1, N):
    cnt = 0
    for i in range(1001):
        cnt += matrix[i].count(n)
    print(cnt)
print(w*h)