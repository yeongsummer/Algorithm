N, M = list(map(int, input().split()))
pan = [input() for _ in range(N)]

answer = []
for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if pan[k][l] == 'W':
                        first_B += 1
                    else:
                        first_W += 1
                else:
                    if pan[k][l] == 'W':
                        first_W += 1
                    else:
                        first_B += 1
        answer.append(min(first_W,first_B))
print(min(answer))