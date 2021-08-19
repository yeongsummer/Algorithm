# 비밀번호

def no_overlap(N, string):
    stack = []
    for i in range(N):
        if not stack:
            stack.append(string[i])
        elif stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])
    return stack

for tc in range(10):
    N, string = input().split()
    print('#{0} {1}'.format(tc+1, ''.join(no_overlap(int(N), list(string)))))