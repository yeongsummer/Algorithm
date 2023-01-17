def solution(new_id):
    new_id = new_id.strip('.')
    answer = ''
    
    flag = True
    for i in range(len(new_id)):
        # 1.
        if new_id[i].isalpha():
            flag = True
            answer += new_id[i].lower()
        # 2. 
        elif new_id[i].isdigit() or new_id[i] in '-_':
            flag = True
            answer += new_id[i]
        # 3.
        elif flag and new_id[i] == '.' :
            answer += '.'
            flag = False
    
    # 4.        
    new_id = new_id.strip('.')
    
    # 5.
    if not answer:
        answer = 'a'
    print(answer)

    # 6.    
    answer = answer[:15]
    answer = answer.strip('.')

    # 7.
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer