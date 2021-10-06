# 세 용액
def two_pointer(lst):
    left, right = 0, N-1
    cnt = 0
    tot = 0
 
    while left < len(a):
        if tot == 0:
            cnt += 1
            tot -= a[left]
            left += 1
        elif tot > 0 or right >= len(a): # 이 부분율 유심히 보길 바란다.
            tot += a[left]
            left += 1
        elif tot < target:
            tot += a[right]
            right += 1
 
    return cnt

N = int(input())
nums = list(map(int,input().split()))
nums.sort()

