from collections import defaultdict

for tc in range(1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))

    G = defaultdict(list)  # 인접리스트
    R = [[] for _ in range(V+1)]  # 각 노드들의 선행 노드 저장해둘 리스트
    for i in range(0, E*2, 2):
        G[edge[i]].append(edge[i+1])
        R[edge[i+1]].append(edge[i])

    stack = []
    for i in range(1, V+1):
        if not R[i]:
            stack.append(i)

    visited = []
    while stack:
        v = stack.pop()
        if v not in visited and len(R[v])== 0: # 방문한 적 없고 선행노드가 없으면 가능
            visited.append(v)

            for i in range(1, V+1):  # 방문했으면 각 노드들의 해당 선행 노드 제거
                if v in R[i]:
                    R[i].remove(v)
            stack += G[v]
    print('#{}'.format(tc),*visited)