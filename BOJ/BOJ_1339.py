N = int(input())
words = []
for _ in range(N):
    words.append(list(input()))
alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

lst = []
for a in alphas:
    total = 0
    for word in words:
        for i, b in enumerate(word[::-1]):
            if a == b:
                total += 10**i
    lst.append((total,a))
lst.sort(reverse=True)

num = 9
for item in lst:
    a = item[1]
    for word in words:
        length = len(word)
        for i in range(length):
            if word[i] == a:
                word[i] = str(num)
    num -= 1
    
ans = 0
for word in words:
    ans += int(''.join(word))
print(ans)




