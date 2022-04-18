from collections import defaultdict, deque

def solution(info, edges):
    def parents_find(x):
        nonlocal valuable

        while x:
            p = parents_dict[x]
            valuable.add(p)
            x = p
        

    def bfs():
        nonlocal sheep_cnt
        temp = -1
        deq = deque([0])
        wolf_cnt = 0

        while deq:
            x = deq.popleft()
            print(x)
            if x == 10:
                break
            if info[x]:
                if sheep_cnt <= wolf_cnt + 1:
                    if temp == x:
                        break
                    deq.append(x)
                    temp = x
                    continue
                else:
                    wolf_cnt += 1
                    print(sheep_cnt, wolf_cnt)
            else:
                sheep_cnt += 1
                print(sheep_cnt, wolf_cnt)

            for i in child_dict[x]:
                if i in valuable:
                    deq.append(i)
            print(deq)


    sheep_cnt = 0
    parents_dict = {}
    child_dict = defaultdict(list)

    valuable = set()

    for edge in edges:
        a, b = edge
        child_dict[a].append(b)
        parents_dict[b] = a

    for i in range(len(info)):
        if not info[i]:
            valuable.add(i)
            parents_find(i)
        
    print(valuable)
    print(child_dict)


    bfs()

    return sheep_cnt

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info, edges))