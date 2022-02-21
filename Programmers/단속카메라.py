from collections import defaultdict
def solution(routes):
    answer = len(routes)
    meet = defaultdict(list)
    for i in range(len(routes)):
        for j in range(i+1, len(routes)):
            if routes[i][1] < routes[j][0] or routes[i][0] > routes[j][1]:
                meet[i].append(routes[j])
                meet[j].append(routes[i])
    print(meet)
    if not meet:
        return 1
    max_cnt = 0
    max_key = []
    for key, value in meet.items():
        if max_cnt < len(value):
            max_cnt = len(value)
            max_key = [key]
        elif max_cnt == len(value):
            max_key.append(key)
    print(max_key)
    for key in max_key:
        val = meet[key]

        result = defaultdict(int)
        for i in range(len(val)):
            for j in range(i+1, len(val)):
                if val[i][1] < val[j][0] or val[i][0] > val[j][1]:
                    result[i] += 1
                    result[j] += 1

        if not result:
            answer = 1+1
        else:
            answer = min(answer, max(result.values()))+2
    
    
        
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0]])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2