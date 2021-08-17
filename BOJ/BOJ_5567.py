N = int(input())
n = int(input())
relationship = [list(map(int,input().split())) for _ in range(n)]
people = [i for i in range(1,N+1)]
friends = []
BF= []

for i in relationship:
    if 1 in i:
        BF += i
for i in relationship:
    for j in BF:
        if j in i:
            friends +=i
print(len(set(friends))-1)