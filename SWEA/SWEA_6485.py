# 삼성시의 버스 노선

def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선수
    bus_route = [list(map(int, input().split())) for _ in range(N)]  # 버스의 노선들을 저장할 리스트

    P = int(input())
    answer = []

    for i in range(P):
        C = int(input())
        answer.append(bus_count(C))

    print('#{}'.format(tc), *answer)