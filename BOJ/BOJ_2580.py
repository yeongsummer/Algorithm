from copy import deepcopy

def sudoku(board):
    global answer, find

    if find:
        return

    flag = False
    for x in range(9):
        for y in range(9):
            if not board[x][y]:
                flag = True
                # 가로
                copy_nums = nums[:]
                for i in range(9):
                    if board[x][i]:
                        copy_nums.remove(board[x][i])
                cand1 = copy_nums

                # 세로
                copy_nums = nums[:]
                for i in range(9):
                    if board[i][y]:
                        copy_nums.remove(board[i][y])
                cand2 = copy_nums

                # 사각형
                copy_nums = nums[:]
                nx, ny = x // 3, y // 3
                for i in range(3):
                    for j in range(3):
                        if board[nx*3+i][ny*3+j]:
                            copy_nums.remove(board[nx*3+i][ny*3+j])
                cand3 = copy_nums

                cand = set(cand1) & set(cand2) & set(cand3)

                if not cand:
                    return
                
                for i in cand:
                    copy_board = deepcopy(board)
                    copy_board[x][y] = i
                    sudoku(copy_board)

                break
        if flag:
            break
    
    if not flag:
        find = 1
        answer = board
        return

board = [list(map(int, input().split())) for _ in range(9)]
nums = [1,2,3,4,5,6,7,8,9]
answer = []
find = 0
sudoku(board)

for i in range(9):
    print(*answer[i])