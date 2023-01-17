T = int(input())
dxy = [(-1,0), (1,0), (0,-1), (0,1)]
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micros = []
    for _ in range(K):
        r, c, cnt, d = map(int, input().split())
        micros.append([r, c, cnt, d])
    
    for _ in range(M):
        for i in range(len(micros)):
            micros[i][0], micros[i][1] = micros[i][0] + dxy[micros[i][3]-1][0] , micros[i][1] + dxy[micros[i][3]-1][1]
            if micros[i][0] == 0 or micros[i][0] == N-1 or micros[i][1] == 0 or micros[i][1] == N-1:
                micros[i][2] = int(micros[i][2]/2)
                if micros[i][3] % 2:
                    micros[i][3] += 1
                else:
                    micros[i][3] -= 1

        matix = [[[0,0] for _ in range(N)] for _ in range(N)]
        remove_list = []
        for i in range(len(micros)):
            if micros[i][2] == 0:
                remove_list.append(i)
                continue
            cnt, idx = matix[micros[i][0]][micros[i][1]]
            if cnt == 0:
                matix[micros[i][0]][micros[i][1]] = [micros[i][2], i]
            else:
                if cnt > micros[i][2]:
                    micros[idx][2] += micros[i][2]
                    remove_list.append(i)
                else:
                    matix[micros[i][0]][micros[i][1]] = [micros[i][2], i]
                    micros[i][2] += micros[idx][2]
                    remove_list.append(idx)
        remove_list.sort()
        for i, n in enumerate(remove_list):
            del micros[n-i]
    total = 0
    for item in micros:
        total += item[2]
    print('#{} {}'.format(tc, total))
