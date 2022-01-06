def solution(stones, k):
    answer=''
    l = len(stones)
    fast_n = float('inf')

    def dfs(stone, n, way):
        nonlocal fast_n, answer
        stack = [(stones, 0, '')]

        while stack:
            stone, n, way = stack.pop()
        
            if n > fast_n:
                continue

            zero_count = stone.count(0)
            if zero_count == l-1 and stone.count(k) == 1:
                if n < fast_n:
                    answer = way
                    fast_n = n
                    continue

                elif n == fast_n:
                    answer = max(answer, way)
                    continue

            elif zero_count > 1:
                continue

            elif zero_count == 1:
                idx = stone.index(0)
                stone[idx] += 1
                for j in range(0,idx):
                    stone[j] -= 1
                for j in range(idx+1,l):
                    stone[j] -= 1
                stack.append((stone, n+1, way+str(idx)))

            else:   
                for i in range(l):
                    new_stone = [stone[i]+1]
                    for j in range(0,i):
                        new_stone.append(stone[j] - 1)
                    for j in range(i+1,l):
                        new_stone.append(stone[j] - 1)
                stack.append((new_stone, n+1, way+str(i)))

    dfs(stones, 0, '')
    if not answer:
        answer = '-1'
    return answer

stones = [4, 2, 2, 1, 4]
k =1
print(solution(stones, k))