def find(pattern, char): # 얼마나 움직일지 결정하는 함수
    for i in range(len(pattern) - 2, -1, -1):
        # 마지막글자와 패턴중 일치하는 숫자가 있다면 그만큼 이동한다.
        if pattern[i] == char:
            return len(pattern) - i - 1
    # 일치하는 글자가 없다면 패턴의 길이만큼 이동한다.
    return len(pattern)

def boyer_moore(pattern, text):
    M = len(pattern)
    N = len(text)
    cnt = N
    i = 0
    # 반복은 최대 긴텍스트 길이 - 작은텍스트 길이
    while i <= N - M:
        j = M - 1

        while j >= 0:
            if pattern[j] != text[i + j]:
                move = find(pattern, text[i + M - 1])
                break
            j = j - 1

        if j == -1:  # 인덱스가 -1이라는 뜻은 모든 글자가 맞았다는 뜻
            cnt -= (M - 1)# 검색 성공
            i += M
        else:  # - 1이 아니라면 글자를 못찾은 것이므로 find에서 넘겨준 값만큼 옆으로 이동
            i += move
    return cnt

T = int(input())
for tc in range(T):
    text, pattern = input().split()
    print('#{0} {1}'.format(tc+1, boyer_moore(pattern, text)))

# T = int(input())
# for tc in range(T):
#     text, pattern = input().split()
#     cnt = text.count(pattern)
#     print('#{0} {1}'.format(tc + 1, len(text) - (len(pattern)-1)*cnt))