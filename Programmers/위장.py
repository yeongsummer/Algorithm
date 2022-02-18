from functools import reduce

def solution(clothes):
    spy = dict()
    for i in clothes:
        if not i[1] in spy.keys():
            spy[i[1]] = 0
        spy[i[1]]+=1
    answer = reduce(lambda x, y: x*(y+1), spy.values(), 1) - 1

    return answer