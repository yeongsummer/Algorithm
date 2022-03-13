# def solution(money, costs):
#     answer = 0
#     units = [1, 5, 10, 50, 100, 500]

#     for i in range(5, 0, -1):
#         unit1, unit2 = units[i], units[i-1]
#         cost1, cost2 = costs[i], costs[i-1]
        
#         if (unit1 // unit2) * cost2 < cost1:
#             continue
#         else:
#             cnt, money = divmod(money, unit1)
#             answer += cnt * cost1

#     answer += money*costs[0]
#     return answer


# money = 4578
# costs = [1, 4, 99, 35, 50, 1000]
# print(solution(money, costs))


# def solution(n, clockwise):
#     board = [[0]*n for _ in range(n)]

#     if clockwise:
#         dx = [0, 1, 0, -1]
#         dy = [1, 0, -1, 0]
#         start = [(0,0), (0, n-1), (n-1, n-1), (n-1, 0)]
#     else:
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
#         start = [(0,0), (n-1, 0), (n-1, n-1), (0, n-1)]

#     for i in range(4):
#         x, y = start[i]
#         board[x][y] = 1
#         temp = 0

#         num = 2
#         for _ in range(n-2):
#             x, y = x + dx[(i+temp)%4], y + dy[(i+temp)%4]
#             board[x][y] = num
#             num += 1
#         temp += 1

#         for c in range(n-3, -1, -2):
#             if c == 0:
#                 c = 1

#             for _ in range(c):
#                 x, y = x + dx[(i+temp)%4], y + dy[(i+temp)%4]
#                 board[x][y] = num
#                 num += 1
#             temp += 1

#     return board


# n = 9
# clockwise = False
# print(solution(n, clockwise))
# from collections import deque

def solution(width, height, diagonals):  
    dp = [[0]*(width+1) for _ in range(height+1)]
    dp[height][0] = 1

    diag_board = [[0]*(width+1) for _ in range(height+1)]
    for diag in diagonals:
        x, y = diag
        nx, ny = height - x, y - 1
        diag_board[nx][ny] = 1
        diag_board[nx+1][ny+1] = 2

    for i in range(height+1):
        print(diag_board[i])

    for i in range(height, -1, -1):
        for j in range(width+1):
            if i == height:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i+1][j]
            else:
                dp[i][j] += dp[i][j-1] + dp[i+1][j]
            if diag_board[i][j] == 1:
                dp[i][j] += dp[i+1][j+1]
            elif diag_board[i][j] == 2:
                dp[i][j] += dp[i-1][j-1]

    for i in range(height+1):
        print(dp[i])

    return dp[0][width]


    diag_board = [[0]*(width+1) for _ in range(height+1)]
    max_x = max_y = 0
    for diag in diagonals:
        x, y = diag
        nx, ny = height - x, y - 1
        diag_board[nx][ny] = 1
        diag_board[nx+1][ny+1] = 2
        max_x = max(max_x, nx+1)
        max_y = max(max_y, ny+1)
    print(max_x, max_y)

    dxy = [(-1,0),(0,1)]
    diag = [(1, 1), (-1,-1)]
    answer = 0
    visited = []
    deq = deque([(height, 0, 0, visited)])
    visited.append((height, 0))

    while deq:
        x, y, d, visited = deq.popleft()

        if (x, y) == (0, width) and d == 1:
            answer += 1
            continue

        if d == 0 and (x < max_x or y > max_y):
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < height + 1 and -1 < ny < width + 1:
                if (nx, ny) not in visited:

                    if not d:
                        deq.append((nx, ny, 0, visited+[(nx, ny)]))
                    else:
                        deq.append((nx, ny, 1, visited+[(nx, ny)]))

        if not d:
            if diag_board[x][y]:
                if diag_board[x][y] == 1:
                    nx, ny = x + diag[0][0], y + diag[0][1]
                elif diag_board[x][y] == 2:
                    nx, ny = x + diag[1][0], y + diag[1][1]

                if -1 < nx < height + 1 and -1 < ny < width + 1:
                    if (nx, ny) not in visited:
                        deq.append((nx, ny, 1, visited+[(nx, ny)]))

    return answer%10000019


width = 2
height = 2
diagonals = [[1,1],[2,2]]
print(solution(width, height, diagonals))
