package programmers

import "math"

func dot(k int, d int) int64 {
	var answer int64
	for i:=0; i<=d/k; i++ {
		n := int64(math.Sqrt(math.Pow(float64(d)/float64(k), 2) - math.Pow(float64(i), 2)))
		answer +=  n + 1
	}
    return answer
}