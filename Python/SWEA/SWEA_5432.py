T = int(input())

for tc in range(T):
    steels = input()
    steels_list = []
    cnt = 0
    i = 0
    while i < len(steels):
        if steels[i] == '(':
            if steels[i+1] != ')':
                steels_list.append(i)
                i += 1
            else:
                cnt += len(steels_list)
                i += 2
        else:
            cnt += 1
            steels_list.pop()
            i += 1
            
    print('#{0} {1}'.format(tc+1, cnt))