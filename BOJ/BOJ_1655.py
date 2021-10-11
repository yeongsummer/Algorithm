import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-n,n))
    else:
        heapq.heappush(min_heap, n)
    
    if min_heap and max_heap[0][1] > min_heap[0]:
        m1 = heapq.heappop(min_heap)
        m2 = heapq.heappop(max_heap)[1]
        heapq.heappush(max_heap, (-m1, m1))
        heapq.heappush(min_heap, m2)

    print(max_heap[0][1])
