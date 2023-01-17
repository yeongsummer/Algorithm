dxy = [(1,1),(1,-1),(-1,-1),(-1,1)]
def dfs(x, y, nums, d):
    global i, j, ans
    stack = [(x, y, nums, d)]
    while stack:
        x, y, nums, d = stack.pop()

        for k in range(d, min(4, d+2)):
            nx, ny = x + dxy[k][0], y + dxy[k][1]

            if -1 < nx < N and -1 < ny < N:
                if nx == i and ny == j:
                    ans = max(ans, len(nums))
                    continue

                if cafes[nx][ny] not in nums:
                    stack.append((nx, ny, nums+[cafes[nx][ny]], k))
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N-1):
        for j in range(N-1):
            if cafes[i][j] != cafes[i+1][j+1]:
                nums = [cafes[i][j], cafes[i+1][j+1]]
                dfs(i+1, j+1, nums, 0)

    print('#{} {}'.format(tc,ans))