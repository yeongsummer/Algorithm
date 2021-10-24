# def section_sum(idx, total):
#     global answer

#     if idx == N:
#         if total < answer:
#             answer = total
#             return

#     if total > answer:
#         return

#     for i in range(N):
#         if i not in visited:
#             visited.append(i)
#             section_sum(idx+1, total+matrix[idx][i])
#             visited.pop()

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     answer = 30
#     visited = []
#     section_sum(0, 0)
#     print('#{} {}'.format(tc, answer))

def min_sum(n, rows, total):
    global ans

    if total > ans:
        return

    if n == N:
        ans = min(ans, total)

    for i in range(N):
        if i not in rows:
            min_sum(n+1, rows+[i], total+matrix[n][i])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 100
    min_sum(0, [], 0)
    print('#{} {}'.format(tc, ans))