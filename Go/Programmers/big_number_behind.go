package programmers

func bigNumberBehind(numbers []int) []int {
	answer := make([]int, len(numbers))
	big_nums := []int{}
	for i := len(numbers) - 1; i > -1; i-- {
		for j := len(big_nums) - 1; j > -1; j-- {
			if numbers[i] < big_nums[j] {
				answer[i] = big_nums[j]
				big_nums = append(big_nums[0:j+1], numbers[i])
				break
			}
		}
		if answer[i] == 0 {
			answer[i] = -1
			big_nums = []int{numbers[i]}
		}
	}
	return answer
}
