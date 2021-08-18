# 메모이제이션 이용

T = int(input())

for tc in range(T):
    n = int(input())
    pascal = [[1]]
    for i in range(1, n):
        lst = [1]
        m = 0
        while m+1 < len(pascal[i-1]):
            lst.append(pascal[i-1][m]+pascal[i-1][m+1])
            m += 1
        lst.append(1)
        pascal.append(lst)
    print('#{}'.format(tc+1))
    for i in range(n):
        print(*pascal[i])