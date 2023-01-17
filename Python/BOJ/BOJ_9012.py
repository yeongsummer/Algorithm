n = int(input())

for _ in range(n):
    answer = 'NO'
    left = 0
    right = 0
    lst=list(input())
    for i in range(len(lst)):
        if right < left: break
        if lst.pop() == ')' : right += 1
        else : left += 1
    if left == right : answer = 'YES'
    print(answer)