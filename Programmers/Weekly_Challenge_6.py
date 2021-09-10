# 복서 정렬하기

def solution(weights, head2head):
    win = []
    n = len(weights)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if head2head[i][j] == 'W' and weights[i] < weights[j]:
                cnt += 1

        fight = n - head2head[i].count('N')
        if fight:
            win_rate = head2head[i].count('W')/fight*100
        else:
            win_rate = 0

        win.append((win_rate, cnt, weights[i], i))            
        win = sorted(win, key=lambda x:(-x[0],-x[1],-x[2],x[3]))

    answer = [i[3]+1 for i in win]
    return answer