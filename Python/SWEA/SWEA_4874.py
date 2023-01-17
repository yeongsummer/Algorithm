def forth(string):
    stack = []
    for i in string:
        if i == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'

        if i in ['+', '-', '*', '/']:
            if len(stack) < 2:
                return 'error'

            a = stack.pop()
            b = stack.pop()
            if i == '+':
                result = b + a
            elif i == '-':
                result = b - a
            elif i == '*':
                result = b * a
            else:
                result = int(b / a)
            stack.append(result)
        else:
            stack.append(int(i))


T = int(input())
for tc in range(1, T + 1):
    string = input().split()
    print('#{} {}'.format(tc, forth(string)))