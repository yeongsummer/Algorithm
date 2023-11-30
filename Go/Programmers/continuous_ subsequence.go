package programmers

import (
	"fmt"
)

func sums(elements []int) int {
	memo := elements
	l := len(elements)
    for i := 1; i < l; i ++ {
		for j := 0; j < l; j ++ {
			memo = append(memo, memo[len(memo)-5] + memo[(j+i) % l])
			fmt.Println(i, j, memo, len(memo))
		}
	}

	trimmed_memo := removeDuplicates(memo)
	fmt.Print(trimmed_memo)
    return len(trimmed_memo)
}

func removeDuplicates(input []int) []int {
	unique := make(map[int]bool)
	result := []int{}

	for _, num := range input {
		if !unique[num] {
			unique[num] = true
			result = append(result, num)
		}
	}

	return result
}