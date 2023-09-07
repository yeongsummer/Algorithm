def solution(cards):
    answer = []
    opened = [0 for _ in range(len(cards))]
    for i in range(len(cards)):
        if not opened[i]:
            cnt = 0
            next = cards[i] - 1
            while not opened[next]:
                cnt += 1
                opened[next] = 1
                next = cards[next] - 1
            answer.append(cnt)
    
    if len(answer) == 1:
        return 0
    else:
        answer.sort(reverse = True)

    return answer[0]*answer[1]
print(solution([8,6,3,7,2,5,1,4]))