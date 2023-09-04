package programmers

import (
	"sort"
)

func seeSaw(weights []int) int64 {
	var answer int
	sort.Ints(weights)
	var prev int;
	for i := 0; i < len(weights)-1; i++ {
		if i > 0 && weights[i] == weights[i-1] {
			prev --
			answer += prev
			continue
		}
		j := findPartner(weights, weights[i], i+1);
		prev = 0
		for ; j > i; j -- {
			if (weights[i] == weights[j]) || (weights[i] * 2 == weights[j]) || weights[i] * 3 == weights[j] * 2 || weights[i] * 4 == weights[j] * 3 {
				prev ++
			}
		}
		answer += prev
	}
    return int64(answer)
}

func findPartner(weights []int, num int, i int) int {
    left := i
    right := len(weights)-1

    for left < right {
        mid := left + (right-left)/2
		if weights[mid] > num * 2 {
			return mid;
		} else {
			left = mid + 1
		}
    }
	return left;
}