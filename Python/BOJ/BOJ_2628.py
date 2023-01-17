N, M = map(int, input().split())
T = int(input())
h_list = [0, M]
v_list = [0, N]
for i in range(T):
    d, n = map(int, input().split())
    if d :
        v_list.append(n)
    else:
        h_list.append(n)
h_list.sort()
v_list.sort()

max_h = 0
for i in range(len(h_list)-1):
    length = h_list[i+1]-h_list[i]
    if length > max_h:
        max_h = length

max_v = 0
for i in range(len(v_list)-1):
    length = v_list[i+1]-v_list[i]
    if length > max_v:
        max_v = length

print(max_h*max_v)
