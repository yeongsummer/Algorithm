def binary_search(arr, target):
    global ans
    left = 0
    right = N - 1

    flag = -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans += 1
            return
        elif arr[mid] > target:
            if flag == 0:
                break
            right = mid - 1
            flag = 0

        else:
            if flag == 1:
                break
            left = mid + 1
            flag = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    find_nums = list(map(int, input().split()))
    nums.sort()
    ans = 0
    for i in find_nums:
        binary_search(nums, i)
    print('#{} {}'.format(tc, ans))