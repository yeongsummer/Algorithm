def solution(grid):
    answer = []
    width = len(grid[0])
    height = len(grid)
    dxy = [(1,0),(-1,0),(0,1),(0,-1)]
    total = width*height*4
    flag = False

    for dx0, dy0 in dxy:
        x, y = 0 , 0
        visited = [[0 for _ in range(width)] for _ in range(height)]
        visited[x][y] = 1
        dx, dy = dx0, dy0
        cycle = 0
        while True:
            if x == 0 and y == 0 and (dx, dy) != (dx0,dy0):
                dxy.remove((dx, dy))
            if cycle != 0 and x == 0 and y == 0 and dx == dx0 and dy == dy0:
                break
            x, y = x + dx, y + dy
            
            if x >= height:
                x = 0
            elif x < 0:
                x = height - 1
            
            if y >= width:
                y = 0
            elif y < 0:
                y = width - 1
                
            visited[x][y] = 1

            if grid[x][y] == 'L':
                dx, dy = -dy, dx
            elif grid[x][y] == 'R':
                dx, dy = dy, -dx
            cycle += 1

        # for i in range(height):
        #     if 0 in visited[i]:
        #         break
        # else: 
        answer.append(cycle)
        
    answer.sort()
    return answer

grid = ["S","S"]
print(solution(grid))

