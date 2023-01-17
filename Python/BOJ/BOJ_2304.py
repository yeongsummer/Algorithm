def center_col_area(columns, max_h):
    lst = []
    for item in columns:
        if item[1] == max_h:
            lst.append(item)
    return (lst[-1][0]-lst[0][0]+1)*max_h

def warehouse(columns, max_h):
    area = height = start = 0
    i = 0
    while True:
        if columns[i][1] > height:
            area += (columns[i][0]-start)*height
            start = columns[i][0]
            height = columns[i][1]
            
            if height == max_h:
                break
        i += 1
    
    height = 0
    start = columns[-1][0]
    i = -1
    while True:
        if columns[i][1] > height:
            area += (start - columns[i][0])*height
            start = columns[i][0]
            height = columns[i][1]
            
            if height == max_h:
                break
        i -= 1
    return area

N = int(input())
columns = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
for item in columns:
    if item[1] > max_h:
        max_h = item[1]

columns.sort()
area = center_col_area(columns, max_h) + warehouse(columns, max_h)
print(area)

    
