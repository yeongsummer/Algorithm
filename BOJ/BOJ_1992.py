N = int(input())
matrix = []
answer = ''

for _ in range(N):
    matrix.append(list(map(int, str(input()))))

def quad_tree(x, y, n):
    global matrix,answer    
    temp = matrix[y][x]
    double_break = False
    
    for i in range(x, x+n):
        if double_break:
            break
            
        for j in range(y, y+n):
            if matrix[j][i] != temp:
                
                answer += "("
                quad_tree(x, y, n//2)
                quad_tree(x + n//2, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                answer += ")"
                
                double_break = True
                break
    
    if not double_break:
        if matrix[y][x] == 1:
            answer += '1'
        else:
            answer += '0'

quad_tree(0,0,N)
print(answer)