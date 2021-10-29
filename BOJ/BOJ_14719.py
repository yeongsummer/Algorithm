H, W = map(int, input().split())
blocks = ''.join(input().split()).strip('0')
blocks = list(map(int, list(blocks)))

total = 0
# b = blocks.pop()
# while blocks:
#     if b > blocks[-1]:
#         total += b - blocks.pop()
#     else:
#         break
# print(blocks)
# b = blocks.pop(0)
# for block in blocks:
#     if b > block:
#         total += b - block
#     else:
#         b = block

l_block, r_block = blocks[0], blocks[-1]
max_block = min(l_block, r_block)
print(max_block)
left, right = 1, len(blocks)-2


while left < right:
    print(left, right)

    if l_block > blocks[left ]:
        total += min(max_block,l_block) - blocks[left]
    else:
        l_block = blocks[left]
    
    if r_block > blocks[right]:
        total += min(max_block,r_block) - blocks[right]
    else:
        l_block = blocks[right]
    print(total)
    left += 1
    right -= 1

print(total)