def func(lst, c):
    cnt = c
    for i in range(len(lst)-1):
        gt = 0
        idx_gt = -1
        for j in range(i, len(lst)):
            if lst[i] < lst[j]:
                if lst[j] >= gt:
                    gt = lst[j]
                    idx_gt = j
        if idx_gt != -1 and cnt:
            idx = []
            for k in range(len(lst)):
                if lst[k] == gt:
                    idx.append(k)
            if len(idx) != 1:
                ltc = -1
                for l in range(idx[0]):
                    if lst[l] < lst[i]:
                        ltc -= 1
                lst[i], lst[idx[ltc]] = lst[idx[ltc]], lst[i]
            else:
                lst[i], lst[idx_gt] = lst[idx_gt], lst[i]
            cnt -= 1
            if cnt == 0:
                return lst
        else:
            if lst != sorted_lst:
                continue
            else:
                if cnt % 2 == 0:
                    return lst
                else:
                    flag = False
                    for m in range(len(lst)-1):
                        if lst[m] == lst[m+1]:
                            flag = True
                    if flag:
                        return lst
                    else:
                        lst[-1], lst[-2] = lst[-2], lst[-1]
                        return lst

T = int(input())
for tc in range(1, T+1):
    nums, cnt = input().split()
    lst = list(map(int, list(nums)))
    sorted_lst = sorted(lst, reverse=True)
    result = []
    answer = func(lst, int(cnt))
    answer = ''.join(list(map(str,answer)))
    print('#{} {}'.format(tc, answer))
