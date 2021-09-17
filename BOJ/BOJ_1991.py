from collections import defaultdict
def preorder(n):
    print(n, end='')
    if dict[n][0] != '.':
        preorder(dict[n][0])
    if dict[n][1] != '.':
        preorder(dict[n][1])

def inorder(n):
    if dict[n][0] != '.':
        inorder(dict[n][0])
    print(n, end='')
    if dict[n][1] != '.':
        inorder(dict[n][1])

def postorder(n):
    if dict[n][0] != '.':
        postorder(dict[n][0])
    if dict[n][1] != '.':
        postorder(dict[n][1])
    print(n, end='')

N = int(input())
dict = defaultdict(list)

for _ in range(N):
    a,b,c = input().split()
    dict[a] = [b, c]

preorder('A')
print()
inorder('A')
print()
postorder('A')