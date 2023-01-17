# 입실 퇴실
def solution(enter, leave):
    answer = []
    result = [[] for _ in range(len(enter))]
    for i in leave:
        lst = enter[:enter.index(i)+1]
        for j in lst:
            result[j-1]+= lst
        enter.remove(i)

    for i in result:
        answer.append(len(set(i))-1)
    return answer
