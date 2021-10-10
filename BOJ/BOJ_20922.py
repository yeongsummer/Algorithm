from collections import defaultdict

def two_pointer(lst):
    ans = 0
    l = 0
    left = right = 0

    while left <= right and right < len(lst):

        if l > ans:
            ans = l

        if count[nums[right]] < K:
            right += 1
            count[nums[right-1]] += 1
            l += 1
        else:
            count[nums[left]] -= 1
            left += 1
            l -= 1
    
    if l > ans:
        ans = l

    return ans

N, K = map(int, input().split())
nums = list(map(int, input().split()))
count = defaultdict(int)
print(two_pointer(nums))

