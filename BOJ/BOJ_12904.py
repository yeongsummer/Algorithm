S = input().rstrip()
T = input().rstrip()

target_l = len(S)
i = len(T)
while i != target_l:
    if T[-1]=='A':
        T = T[:-1]
    else:
        T = T[-1:0:-1]
    i -= 1

if S == T:
    print(1)
else:
    print(0)
