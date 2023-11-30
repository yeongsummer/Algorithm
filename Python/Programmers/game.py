import heapq

def solution(n, k, enemy):
    answer = 0
    moojuk = []
     
    for ene in enemy:
        n -= ene
        if n >= 0:
            heapq.heappush(moojuk, -ene)
        else:
            if k > 0:
                k -= 1
                heapq.heappush(moojuk, -ene)
                n -= heapq.heappop(moojuk)
            else:
                break
            
        answer += 1

    