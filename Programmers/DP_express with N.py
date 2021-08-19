# 동적계획법
# N으로 표현

def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9) :
        all_case = {int(str(N)*i)}
        
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
                        
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case)         
    return answer