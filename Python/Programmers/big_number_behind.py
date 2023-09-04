def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    big_nums = []
    for i in range(len(numbers)-1, -1, -1) :
        for j in range(len(big_nums)-1, -1, -1):
            if numbers[i] < big_nums[j] :
                answer[i] = big_nums[j] 
                big_nums = big_nums[:j+1] + [numbers[i]]
                break
        else :
            big_nums = [numbers[i]]
    return answer