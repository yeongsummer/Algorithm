from collections import defaultdict

def dfs(n, m, d):
    if n == m:
        print(d)
        return
    visited.append(n)

    for i in node[n]:
        if i not in visited:
            for key in dist.keys():
                if str(n) in key and str(i) in key:
                    dfs(i, m, d + dist[key])
                    break

N, M = map(int, input().split())
node = defaultdict(list)
dist = {}
for _ in range(N-1):
    n1, n2, d = map(int, input().split())
    dist[str(n1)+str(n2)] = d
    node[n1].append(n2)
    node[n2].append(n1)
    
for _ in range(M):
    n1, n2 = map(int, input().split())
    visited = []
    dfs(n1, n2, 0)

