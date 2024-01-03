package main

import (
	"fmt"
)

func main() {
	fmt.Println(hailstone(5, [][]int{{0,0},{0,-1},{2, -3},{3,-3}}))
}

func hailstone(k int, ranges [][]int) []float64 {
	answer := []float64{}
	cumulative_areas := []float64{0.0}
	area := 0.0
    for k != 1 {
		old_k := k
		if k % 2 == 0 {
			k = k/2
		} else {
			k = k*3 + 1
		}
		area = area + (float64(old_k) + float64(k)) / float64(2)
		cumulative_areas = append(cumulative_areas, area)
	}
	
	n := len(cumulative_areas) - 1
	fmt.Println(cumulative_areas)
	for _, r := range ranges {
		if r[0] > n + r[1] {
			answer = append(answer, float64(-1))
		} else {
			answer = append(answer, cumulative_areas[n + r[1]] - cumulative_areas[r[0]])
		}
	}
    return answer
}