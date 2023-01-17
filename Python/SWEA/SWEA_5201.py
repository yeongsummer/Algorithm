T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    goods.sort()
    trucks.sort()
    ans = 0
    while trucks and goods:
        truck = trucks.pop()
        a = goods.pop()
        if truck >= a:
            ans += a
        else:
            trucks.append(truck)
    print('#{} {}'.format(tc, ans))
