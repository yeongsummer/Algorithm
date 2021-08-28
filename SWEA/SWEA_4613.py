T = int(input())
for i in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    color = {0:'W', N-1:'R'}
    cnt_list = []

    # first_cnt = 0
    # for row, c in color.items():
    #     first_cnt += M - flag[row].count(c)
    w_cnt = 0
    for i in range(0, N-2): # 화이트
        w_cnt += M - flag[i].count('W')

        b_cnt = 0
        for j in range(i+1,N-1): # 블루
            b_cnt += M - flag[j].count('B')

            r_cnt = 0
            for k in range(j+1, N): # 레드
                r_cnt += M - flag[k].count('R')

            cnt_list.append(w_cnt + b_cnt + r_cnt)
    print(cnt_list)
    print(min(cnt_list))




        

