def sudoku():
    for i in range(9):
        row_list = []
        col_list = []
        for j in range(9):

            if matrix[i][j] in row_list:
                return 0
            else:
                row_list.append(matrix[i][j])

            if matrix[j][i] in col_list:
                return 0
            else:
                col_list.append(matrix[j][i])

            if i % 3 == 0 and j % 3 == 0:
                square_list = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if matrix[r][c] in square_list:
                            return 0
                        else:
                            square_list.append(matrix[r][c])
    return 1


T = int(input())
for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sudoku()))