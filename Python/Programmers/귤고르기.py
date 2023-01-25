from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    cnt_dic = defaultdict(int)
    
    for v in tangerine :
        cnt_dic[v] += 1
        
    cnt_list = list(cnt_dic.values())
    cnt_list.sort(reverse=True)
    for i in cnt_list :
        k -= i
        answer += 1
        
        if k <= 0 :
            break
         
    return answer