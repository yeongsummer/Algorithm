n = int(input())
result = []
stack = []
count = 0
X = True

for _ in range(n):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')
    
    if stack[-1]== num:
        stack.pop()
        result.append('-')
    else:
        X = False
if X :
    for i in result:
        print(i)
else : print('NO')