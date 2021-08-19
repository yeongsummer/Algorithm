# 괄호 검사
# stack 이용
def brackets_check(string):
    stack = []
    for i in string:
        if i in ['(', '{']:
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                return 0
        elif i == '}':
            if not stack or stack.pop() != '{':
                return 0
    if stack:
        return 0
    return 1

T = int(input())
for tc in range(T):
    string = input()
    print('#{0} {1}'.format(tc+1, brackets_check(string)))