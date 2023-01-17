 # 반복문자 지우기
 # stack 이용

def no_overlap(string):
    stack = []
    while string:
        if not stack:
            stack.append(string.pop(0))
        if stack[-1] == string[0]:
            stack.pop()
            string.pop(0)
        else:
            stack.append(string.pop(0))
    return len(stack)

T = int(input())

for tc in range(T):
    string = input()
    print('#{0} {1}'.format(tc+1, no_overlap(list(string))))