# 5주차_모음사전

a = {'A':1,'E':2,'I':3,'O':4,'U':5}
def solution(word):
    length = len(word)
    answer = length
    w = []
    
    for i in range(5):
        if i < length:
            w.append(a[word[i]])
        else:
            w.append(0)
    
    temp = 0
    for i in w[::-1]:
        temp = temp*5+1
        if i :
            answer += (i-1)*temp
    return answer