for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    result = ''
    for i in string:
        if i.isdigit():
            result += i
        else:
            if i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack:
                    result += stack.pop()
                stack.append(i)
    while stack:
        result += stack.pop()

    stack = []
    for i in result:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(i))

    print('#{} {}'.format(tc, stack.pop()))
