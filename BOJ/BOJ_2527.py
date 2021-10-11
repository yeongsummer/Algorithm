for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    lst = [(a, b, c, d), (e, f, g, h)]
    lst.sort()
    x1, y1, p1, q1 = lst[0]
    x2, y2, p2, q2 = lst[1]
    result = 'd'
    if p1 > x2:
        if y1 <= y2 < q1:
            result = 'a'
        elif y2 < y1 and q2 > y1:
            result = 'a'
        elif y2 == q1 or q2 == y1:
            result = 'b'
    elif p1 == x2:
        if y2 == q1 or q2 == y1:
            result = 'c'
        elif y2 < q1 and y1 < q2:
            result = 'b'
    print(result)
    

