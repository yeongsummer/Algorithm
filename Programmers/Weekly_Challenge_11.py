def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    cnt = len(rectangle)
    point = []
    total1 = 
    point1 = []
    point2 = []
    for i in range(cnt):
        s_x, s_y, e_x, e_y = rectangle[i]
        candidates = [(s_x, s_y), (e_x,s_y), (s_x, e_y), (e_x, e_y)]
        for cand in candidates:
            x, y = cand
            for j in range(cnt):
                if i != j:
                    if rectangle[j][0] < x < rectangle[j][2] and rectangle[j][1] < y < rectangle[j][3]:
                        break
            else:
                point.append((x,y))

                                             
    return answer
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
solution(rectangle, 1, 3, 7, 8)