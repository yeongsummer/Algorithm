def solution(meeting):
    answer = 0
    endTime = 0
    for i in range(len(meeting)):
        if endTime <= meeting[i][0]:
            endTime = meeting[i][1]
            answer += 1
    return answer

N = int(input())
meeting = [list(map(int,input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

print(solution(meeting))