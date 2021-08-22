# 참외밭

direction = {4:2, 2:3, 3:1, 1:4}
K = int(input())
area = [list(map(int,input().split())) for _ in range(6)]

result = []
empty = 0
for i in range(5):
    if direction[area[i][0]] == area[i+1][0]:
        result.append(area[i][1]*area[i+1][1])
    else:
        empty = area[i][1]*area[i+1][1]
if empty:
    result.append(area[0][1]*area[5][1])
else:
    empty = area[0][1]*area[5][1]

print((max(result)-empty)*K)