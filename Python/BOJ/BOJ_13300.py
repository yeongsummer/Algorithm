# 방배정

number, N = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(number)]

room = [[0, 0] for _ in range(6)]
count = 0
for i in people:
    room[i[1]-1][i[0]] += 1
for i in range(6):
    for j in range(2):
        count += int(room[i][j]//N)
        if room[i][j]%N:
            count+=1