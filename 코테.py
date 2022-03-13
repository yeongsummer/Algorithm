from collections import defaultdict

def solution(H):

    def update(i, x):
        while i <= l:
            print(i)
            tree[i] = min(tree[i], x)
            i += (i & -i)

    def update2(i, x):
        while i > 0:
            print(i)
            tree2[i] = min(tree2[i], x)
            i -= (i & -i)

    def query(a, b):
        v = MAX

        prev = a
        curr = prev + (prev & -prev)
        while curr <= b:
            v = min(v, tree2[prev])
            prev = curr
            curr = prev + (prev & -prev)

        v = min(v, arr[prev])

        prev = b
        curr = prev - (prev & -prev)
        while curr >= a:
            v = min(v, tree[prev])
            prev = curr
            curr = prev - (prev & -prev)

        return v

    answer = []
    l = len(H)  
    MAX = 100000001
    arr = [0] * (l+1)
    tree = [MAX] * (l+2)
    tree2 = [MAX] * (l+2)
    rec = defaultdict(int)

    for i in range(1, l+1):
        arr[i] = H[i-1]
        update(i, arr[i])
        update2(i, arr[i])

    for i in range(1, l+1):
        for j in range(i, l+1):
            print(i, j)
            rec[query(i, j)] += 1


    for key, value in rec.items():
        answer.append([key, value])

    answer.sort()
    return answer


H = [3,2,1,1,3]
print(solution(H))