T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    c = N//2
    total = sum(farm[c])
    for i in range(c):
        total += sum(farm[i][c-i:c+i+1]) + sum(farm[-i-1][c-i:c+i+1])
    print('#{} {}'.format(tc, total))