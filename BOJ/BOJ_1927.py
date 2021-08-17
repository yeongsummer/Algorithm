import sys
import heapq as hq

N = int(input())
heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X :
        hq.heappush(heap,(X))
    else:
        try:print(hq.heappop(heap))
        except:print(0)