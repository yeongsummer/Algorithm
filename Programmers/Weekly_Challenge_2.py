def solution(scores):
    N = len(scores)
    answer = ''
    score_sum = [0 for i in range(N)]
    student = [N for i in range(N)]
    
    for i in range(N):
        sccores_T = list(zip(*scores))[i]
        if scores[i][i] in [max(sccores_T), min(sccores_T)] and sccores_T.count(scores[i][i])==1:
            scores[i][i] = 0
            student[i] -= 1
        score_sum = [x + y for x, y in zip(score_sum,scores[i])]
    avg_list = [x / y for x, y in zip(score_sum,student)]
    
    for i in avg_list:
        if i >= 90 :
            answer += 'A'
        elif i >= 80 :
            answer += 'B'
        elif i >= 70 :
            answer += 'C'
        elif i >= 50 :
            answer += 'D'
        else:
            answer += 'F'
    return answer