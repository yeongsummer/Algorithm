import math

def solution(n, k):
    answer = 0
    num = convert(n, k) + '0'
    tmp = ''
    for i in num:
        if i != '0':
            tmp += i
        else:
            if len(tmp) != 0:
                if is_prime_number(int(tmp)):
                    answer += 1
                tmp = ''
    return answer

def convert(n, k):
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result = str(mod) + result
    return result

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True