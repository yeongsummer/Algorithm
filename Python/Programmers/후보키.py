from itertools import combinations

def solution(relation):
    C = len(relation[0])
    cand = []
    cols = [i for i in range(C)]

    for i in range(1, C+1):
        for combi in combinations(cols, i):
            for i in range(len(cand)):
                if set(cand[i]).issubset(set(combi)):
                    break

            else:
                data = []
                for relat in relation:
                    temp = []
                    for j in combi:
                        temp.append(relat[j])
                    
                    if temp in data:
                        break
                    else:
                        data.append(temp)
                else:
                    cand.append(combi)

    return len(cand)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))