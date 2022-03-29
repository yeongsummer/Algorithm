sudoku = [list(map(int, input().split())) for _ in range(9)]
nums = [1,2,3,4,5,6,7,8,9]

flag = True
while flag:
    flag = False

    for x in range(9):
        for y in range(9):
            if not sudoku[x][y]:
                # 가로
                copy_nums = nums[:]
                for i in range(9):
                    if sudoku[x][i]:
                        copy_nums.remove(sudoku[x][i])
                cand1 = copy_nums

                # 세로
                copy_nums = nums[:]
                for i in range(9):
                    if sudoku[i][y]:
                        copy_nums.remove(sudoku[i][y])
                cand2 = copy_nums

                # 사각형
                copy_nums = nums[:]
                nx, ny = x // 3, y // 3
                for i in range(3):
                    for j in range(3):
                        if sudoku[nx*3+i][ny*3+j]:
                            copy_nums.remove(sudoku[nx*3+i][ny*3+j])
                cand3 = copy_nums

                cand = set(cand1) & set(cand2) & set(cand3)

                if len(cand) == 1:
                    sudoku[x][y] = list(cand)[0]
                    flag = True

for i in range(9):
    print(*sudoku[i])
