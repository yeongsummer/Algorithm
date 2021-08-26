import sys
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    pizza = [[i+1, p] for i, p in enumerate(pizza_list)]
    fire = pizza[:N]
    remain = pizza[N:]

    while len(fire) > 1:
        cheese = fire.pop(0)
        if cheese[1]//2 != 0:
            cheese[1] = cheese[1]//2
            fire.append(cheese)
        else:
            if remain:
                fire.append(remain.pop(0))
    print('#{} {}'.format(tc, fire[0][0]))
