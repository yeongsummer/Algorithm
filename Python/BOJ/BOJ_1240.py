from collections import defaultdict, deque

def bfs(n, m):
    deq = deque()
    deq.append([n, 0])
    visited[n] = 1
    while deq:
        n, d = deq.popleft()
        for item in node[n]:
            new_d = d+item[1]
            if item[0] == m:
                return new_d
            else:
                if visited[item[0]] == 0:
                    visited[item[0]] = 1
                    deq.append((item[0], new_d))

N, M = map(int, input().split())
node = defaultdict(list)

for _ in range(N-1):
    n1, n2, d = map(int, input().split())
    node[n1].append((n2, d))
    node[n2].append((n1, d))

for _ in range(M):
    n1, n2 = map(int, input().split())
    visited = [0] * (N+1)
    print(bfs(n1, n2))

