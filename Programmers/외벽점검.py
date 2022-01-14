from itertools import permutations

def solution(n, weak, dist):
    answer = float('inf')
    gap = []
    l = len(weak)

    for i in range(l-1):
        gap.append(weak[i+1] - weak[i])
    gap.append(n - weak[l-1] + weak[0])
    print(gap)

    for perm in permutations(dist, len(dist)):
        fix = [0] * l
        cnt = 0
        print(perm)
        for p in perm:
            print(p)
            m = p
            for i in range(len(gap)):
                if gap[i] <= m and not fix[i] and not fix[(i+1)//4]:
                    fix[i] = 1
                    m -= gap[i]
                    if m < gap[i+1]:
                        fix[i+1] = 1
                        cnt += 1
                        break
                print(fix)
                if sum(fix) == l:
                    answer = min(answer, cnt)
                    break

    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))