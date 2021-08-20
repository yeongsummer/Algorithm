# 어디에 단어가 들어갈 수 있을까

def rotate(N, matrix):
    matrix90 = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix90[j][N - 1 - i] = matrix[i][j]

    return matrix90

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    # 처음 퍼즐 그대로 행 검사 후, 90도 회전시킨뒤 행을 검사하면 열검사까지 가능
    for _ in range(2):
        for i in range(N):
            cnt_r = 0
            for j in range(N):
                if puzzle[i][j] == 1:
                    cnt_r += 1
                else:
                    if cnt_r == K:
                        answer += 1
                    cnt_r = 0

            if cnt_r == K:
                answer += 1

        puzzle = rotate(N, puzzle)
    print('#{} {}'.format(tc + 1, answer))