def bottom_index(i):
    if i == 0:
        return -1
    else:
        return (i + 1) % 4 + 1

def max_finder(i, array):
    lst = array[:]
    b_index = bottom_index(i)
    bottom = lst[b_index]
    lst[i] = 0
    lst[b_index] = 0

    return bottom, max(lst)

N = int(input())
dice_list =[list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(len(dice_list[0])):
    total = 0
    bottom, max_sum = max_finder(i, dice_list[0])
    total += max_sum

    for dice in dice_list[1:]:
        t_index = dice.index(bottom)
        bottom, max_sum = max_finder(t_index, dice)
        total += max_sum

    if total > answer:
        answer = total

print(answer)

