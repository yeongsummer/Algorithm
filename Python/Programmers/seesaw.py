from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)

    for i in range(100, 1001):
        if counter[i] > 0:
            answer += counter[i] * (counter[i] - 1) // 2
            answer += counter[i] * counter[i * 3 / 2]
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 4 / 3]

    return answer