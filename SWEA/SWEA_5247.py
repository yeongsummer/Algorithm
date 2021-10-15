from collections import deque

def bfs(n, c):
    deq = deque([(n, c)])
    visited = set()
    visited.add(n)

    while deq:
        n, c = deq.popleft()

        # if n > 1000000:
        #     continue

        if n == M:
            return c

        if n*2 not in visited and n*2 <= 1000000:
            deq.append((n*2, c+1))
            visited.add(n*2)
        if n+1 not in visited and n+1 <= 1000000:
            deq.append((n+1, c+1))
            visited.add(n+1)
        if n-1 not in visited and n-1 <= 1000000:
            deq.append((n-1, c+1))
            visited.add(n-1)
        if n-10 not in visited and n-10 <= 1000000:
            deq.append((n-10, c+1))
            visited.add(n-10)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, bfs(N, 0)))