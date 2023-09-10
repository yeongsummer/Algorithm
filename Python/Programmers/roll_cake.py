def solution(topping):
    answer = 0
    front_cnt = [0 for _ in range(10001)]
    back_cnt = [0 for _ in range(10001)]
    
    for t in topping:
        back_cnt[t] += 1
    front_total, back_total = 0, len(set(topping))

    for i in topping:
        if not front_cnt[i]:
            front_total += 1

        front_cnt[i] += 1
        back_cnt[i] -= 1

        if not back_cnt[i]:
            back_total -= 1

        if front_total == back_total:
            answer += 1
        elif front_total > back_total:
            break

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))