# 최소직사각형

def solution(sizes):
    len1 = max(max(size) for size in sizes)
    len2 = max(min(size) for size in sizes)
    answer = len1 * len2
    return answer