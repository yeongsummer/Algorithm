dp = {1:1,2:2,3:4}
def illesam1(n):
    if not dp.get(n) :
        answer =  illesam1(n-1)+illesam1(n-2)+illesam1(n-3)
        dp[n] = answer
        return answer
    else :
        return dp[n]

n = int(input())
while n != 0:
    k = int(input())
    print(illesam1(k))
    n-=1