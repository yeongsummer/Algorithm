T = int(input())
number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(T):
unnecessary_string = input()
num_list = input().split()
new_list = []

for i in number:
new_list += [i] * num_list.count(i)

print('#{}'.format(tc+1))
print(*new_list)
