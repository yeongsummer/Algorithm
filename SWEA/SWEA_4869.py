# DP 이용
def paper(n):
    lst = [1, 1]

    for i in range(20, n+1, 10):
        i //= 10
        lst.append(lst[i-2]+2**(i-1))

    return lst[n//10]

T = int(input())

for tc in range(T):
    n = int(input())
    print('#{0} {1}'.format(tc+1, paper(n)))