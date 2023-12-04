package main

import (
	"fmt"
)

func main() {
	fmt.Println(queue_sum([]int{2,3,2}, []int{1,1,1}))
}

func queue_sum(queue1 []int, queue2 []int) int {
	answer := 0
	queue := append(queue1, queue2...)
	total_sum := 0
	for _, n := range queue {
		total_sum += n
	}

	if total_sum % 2 > 0 {
		return -1
	}

	target_sum := total_sum/2
	interval_sum := 0
	for _, n := range queue1 {
		interval_sum += n
	}
	start, end := 0, len(queue1)
	l := len(queue)

	for end < l {
		for start < l && interval_sum > target_sum {
			interval_sum -= queue[start]
			start ++
			answer += 1
		}

		if interval_sum == target_sum {
			return answer
		}

		interval_sum += queue[end]
		end ++
		answer ++
	}
	
    return -1
}