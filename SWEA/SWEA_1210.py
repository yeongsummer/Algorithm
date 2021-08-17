for _ in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]
    line = list(filter(lambda x: matrix[0][x] == 1, range(100))) # 세로축 찾기

    target = matrix[-1].index(2) # 시작 세로축의 위치 찾기
    target_index = line.index(target)

    i = -2
    while i > -100: # 아래에서부터 올라감
        if target > 1 and matrix[i][target-1] == 1: # 왼쪽으로 먼저 가지가 뻗어있으면 왼쪽 세로축으로 이동
            target_index -= 1
            target = line[target_index]
        elif target < 99 and matrix[i][target+1] == 1: # 오른쪽으로 먼저 가지가 뻗어있으면 오른쪽 세로축으로 이동
            target_index += 1
            target = line[target_index]
        i -= 1

    print('#{0} {1}'.format(T, target))