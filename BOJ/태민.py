def switch_on_off():
    for i in range(std_num):
        if std_list[i][0] == 1:  # 남자일 때,
            for j in range(std_list[i][1]-1, switch_num, std_list[i][1]):
                if switch_arr[j] == 0:
                    switch_arr[j] = 1
                else:
                    switch_arr[j] = 0
            print(switch_arr)

        elif std_list[i][0] == 2:
            cnt = 0
            while std_list[i][1]-2-cnt >= 0 and std_list[i][1]+cnt < switch_num:
                if switch_arr[std_list[i][1]-2-cnt] == switch_arr[std_list[i][1]+cnt]:
                    cnt += 1
                else:
                    break
            for x in range(std_list[i][1]-1-cnt, std_list[i][1]+cnt):
                if switch_arr[x] == 1:
                    switch_arr[x] = 0
                else:
                    switch_arr[x] = 1

    for k in range(switch_num):  # 20개씩 출력
        print(switch_arr[k], end=' ')
        if not (k + 1) % 20:
            print()

switch_num = int(input())
switch_arr = list(map(int, input().split()))
std_num = int(input())
std_list = [list(map(int, (input().split()))) for _ in range(std_num)]
switch_on_off()
