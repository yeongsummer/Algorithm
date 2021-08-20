# 의석이의 세로로 말해요

T = int(input())
for tc in range(T):
    string_list = [list(input()) for _ in range(5)]
    result = []
    for string in string_list:
        for i in range(len(string)):
            if i >= len(result):
                result.append(string[i])
            else:
                result[i] += string[i]
    print('#{}'.format(tc+1), ''.join(result))