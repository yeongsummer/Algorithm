# 색종이

N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(89-b, 99-b):
            paper[j][i] = 1
total = 0
for i in range(100):
    total += paper[i].count(1)
print(total)

