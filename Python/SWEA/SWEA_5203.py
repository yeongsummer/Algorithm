def babygin(lst, i):
    if lst[i] >= 3:
        return True
    if lst[i - 2] and lst[i - 1] and lst[i]:
        return True
    if i < 8 and lst[i] and lst[i + 1] and lst[i + 2]:
        return True
    if i < 9 and lst[i - 1] and lst[i] and lst[i + 1]:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    num_counts1 = [0] * 10
    num_counts2 = [0] * 10

    i = 0
    ans = 0
    for i in range(0, 12):
        if i % 2 == 0:
            num_counts1[nums[i]] += 1
            if babygin(num_counts1, nums[i]):
                ans = 1
                break
        else:
            num_counts2[nums[i]] += 1
            if babygin(num_counts2, nums[i]):
                ans = 2
                break
    print('#{} {}'.format(tc, ans))




