def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parents[root_y] = root_x
    return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    union_list = list(map(int, input().split()))

    nodes = [i for i in range(1, N + 1)]
    parents = [i for i in range(N + 1)]

    for i in range(0, M*2, 2):
        union(union_list[i], union_list[i+1])

    root = set()
    for node in nodes:
        root.add(find_set(node))

    print('#{} {}'.format(tc, len(root)))