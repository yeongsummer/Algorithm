from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    total_count = 0
    fruits_dict = defaultdict(int)

    for fruit, count in zip(want, number):
        fruits_dict[fruit] = count
        total_count += count

    for fruit in discount[:10]:
        if fruit in fruits_dict:
            fruits_dict[fruit] -= 1
            if fruits_dict[fruit] >= 0:
                total_count -= 1

    if total_count == 0:
        answer += 1

    if len(discount) == 10 :
        return answer

    for i in range(10, len(discount)):
        if discount[i] in fruits_dict:
            fruits_dict[discount[i]] -= 1
            if fruits_dict[discount[i]] >= 0:
                total_count -= 1
        if discount[i-10] in fruits_dict:
            fruits_dict[discount[i-10]] += 1
            if fruits_dict[discount[i-10]] > 0:
                total_count += 1
        if total_count == 0 :
            answer += 1

    return answer