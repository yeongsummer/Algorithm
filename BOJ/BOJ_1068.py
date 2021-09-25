def cut(n):
    if len(tree[n]) == 1:
        tree[n] = [-2]
        return
    else:
        lst = tree[n]
        tree[n] = [-2]
        for i in lst:
            if i != parents[n]:
                cut(i)

def count():
    cnt = 0
    for i in range(len(tree)):
        if len(tree[i]) == 1:
            if tree[i] != [-2]:
                cnt += 1
        else:
            for j in tree[i]:
                if j != parents[i] and tree[j] != [-2]:
                    break
            else:
                cnt += 1
    return cnt


N = int(input())
nodes = list(map(int, input().split()))
n = int(input())
parents = []
tree=[[] for _ in range(N)]
for i in range(N):
    tree[i].append(nodes[i])
    parents.append(nodes[i])
    if nodes[i] != -1:
        tree[nodes[i]].append(i)

cut(n)
print(count())

