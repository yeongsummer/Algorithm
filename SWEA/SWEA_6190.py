# 정곤이의 단조증가함수

def find(numbers):
    global N
    max_num = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]

            if num > max_num:
                num_s = str(num)
                for k in range(len(num_s) - 1):
                    if num_s[k] > num_s[k + 1]:
                        break
                else:
                    max_num = num
    return max_num

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, find(numbers)))