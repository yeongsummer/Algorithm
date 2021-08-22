def bingo_func(bingo, numbers):
    cnt = 0
    for i,number in enumerate(numbers):
        for row in range(5):
            # 선언한 숫자 0으로 바꾸기
            if number in bingo[row]:
                col = bingo[row].index(number)
                bingo[row][col] = 0

                temp1 = temp2 = False
                # 대각선 봐야할지 확인
                if row == col:
                    diagonal1_total = 0
                    temp1 = True

                # 역대각선 봐야할지 확인
                if row + col == 4:
                    diagonal2_total = 0
                    temp2 = True

                col_total = 0
                # 가로, 대각선, 역대각선
                for k in range(5):
                    col_total += bingo[k][col]
                    if temp1:
                        diagonal1_total += bingo[k][k]
                    if temp2:
                        diagonal2_total += bingo[k][4-k]
                
                # count하기
                if sum(bingo[row]) == 0:
                    cnt += 1
                if col_total == 0:
                    cnt += 1
                if temp1:
                    if diagonal1_total == 0:
                        cnt += 1
                if temp2:
                    if diagonal2_total == 0:
                        cnt += 1
                break
        if cnt >= 3:
            return i+1    


bingo = [list(map(int, input().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))
print(bingo_func(bingo, numbers))