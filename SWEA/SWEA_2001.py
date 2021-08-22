# T = int(input())

# for tc in range(T):
#     N, target_num = map(int, input().split())
#     area = [list(map(int, input().split())) for i in range(N)]
#     result_list = []

#     for i in range(N - target_num + 1):
#         for j in range(N - target_num + 1):
#             result = 0
#             for k in range(target_num):
#                 result += sum(area[i + k][j:j + target_num])
#             result_list.append(result)

#     print('#{0} {1}'.format(tc+1, max(result_list)))

# T = int(input())

# for tc in range(T):
#     N, target = map(int, input().split())
#     area = [list(map(int, input().split())) for i in range(N)]
#     result_list = []

#     max_total = 0
#     for i in range(N - target + 1):
#         for j in range(N - target + 1):
#             total = 0
#             for k in range(target):
#                 for l in range(target):
#                     total += area[i + k][j + l]

#             if total > max_total:
#                 max_total = total

#     print('#{0} {1}'.format(tc+1, max_total))

def fly(area, N, M):
    max_total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                total += sum(area[i+k][j:j+M])
            if total > max_total:
                max_total = total
    return max_total
                
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for i in range(N)]
    print('#{0} {1}'.format(tc+1, fly(area, N, M)))