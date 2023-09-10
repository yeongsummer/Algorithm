def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x : (x[col-1], -x[0]))
    sums = []
    for i in range(row_begin, row_end+1):
        sum = 0
        for d in sorted_data[i-1]:
            sum += d % i
        sums.append(sum)
        
    answer = sums[0]
    for i in sums[1:]:
        answer = answer ^ i
        
    return answer