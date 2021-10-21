from itertools import combinations

def solution(line):
    point = []
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')

    for item in combinations(line, 2):
        A, B, E = item[0]
        C, D, F = item[1]
        if A*D == B*C:
            continue
        px = (B*F-E*D)/(A*D-B*C)
        py = (E*C-A*F)/(A*D-B*C)

        if not px % 1 and not py % 1:
            px, py = int(px), int(py)
            point.append((px, py))

            min_x = min(min_x, px)
            max_x = max(max_x, px)
            min_y = min(min_y, py)
            max_y = max(max_y, py)

    matrix = [['.' for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    for p in point:
        x, y = p[0] - min_x, max_y - p[1]
        matrix[y][x] = '*'

    answer = []
    for m in matrix:
        answer.append(''.join(m))

    return answer