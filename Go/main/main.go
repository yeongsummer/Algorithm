package main

import (
	"fmt"
)

func main() {
	fmt.Println(archery(1, []int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}))
}

func archery(n int, info []int) []int {
	answer := &[]int{}
	total := 0
	findWin(0, n, make([]int, 11), info, &total, answer)
	if total == 0 {
		return []int{-1}
	}
    return *answer
}

func findWin(i int, n int, cnts []int, info []int, total *int, answer *[]int) {
	if i == 10 {
		cnts[i] = n
		t := 0
		for i, c := range cnts {
			if info[i] > c {
				t -= 10 - i
			} else if info[i] < c {
				t += 10 - i
			}
		}
		if t < *total {
			return
		} else if t == *total && t != 0 {
			a_i, a_c := findLow(*answer)
			c_i, c_c := findLow(cnts)
			if c_i <= a_i || (c_i == a_i && c_c <= a_c) {
				return
			}
		}
		*total = t
		copyCnts := make([]int, len(cnts))
		copy(copyCnts, cnts)
		*answer = copyCnts
		return
	}
	if info[i] < n {
		cnts[i] = info[i] + 1
		findWin(i+1, n - cnts[i], cnts, info, total, answer)
		cnts[i] = 0
	}
	findWin(i+1, n, cnts, info, total, answer)
}

func findLow(cnts []int) (int, int) {
	for i := 10; i >= 0; i-- {
		if cnts[i] != 0 {
			return i, cnts[i]
		}
	}
	return -1, -1
}