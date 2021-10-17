T = int(input())
for tc in range(1, T+1):
    N, jinsu16 = input().split()
    jinsu2 = ''
    for i in range(int(N)):
        if jinsu16[i].isalpha():
            change = format((ord(jinsu16[i])-55),'b')
        else:
            change = format(int(jinsu16[i]), 'b')
        jinsu2 += '0'*(4-len(change)) + change
    print('#{} {}'.format(tc, jinsu2))