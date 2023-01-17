# 정식이의 은행 업무

def bank(jinsu2, jinsu3):
    originals = []

    for i in range(1, len(jinsu2)):
        original = list(jinsu2)
        if jinsu2[i] == '0':
            original[i] = '1'
        else:
            original[i] = '0'
        originals.append(int(''.join(original), 2))

    nums = ['0', '1', '2']
    for i in range(len(jinsu3)):
        for j in nums:
            original = list(jinsu3)
            if original[i] != j:
                original[i] = j
                original = int(''.join(original), 3)
                if original in originals:
                    return original

T = int(input())
for tc in range(1, T+1):
    jinsu2 = input()
    jinsu3 = input()
    num = bank(jinsu2, jinsu3)
    print('#{} {}'.format(tc, num))
