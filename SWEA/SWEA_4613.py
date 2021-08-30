T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    cnt_list = []

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
    
    print('#{} {}'.format(tc, min(cnt_list)))




        

