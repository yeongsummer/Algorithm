package programmers

import (
	"math"
)

func different_bit(numbers []int64) []int64 {
    answer := []int64{}
    for _, n := range numbers {
        if n == 0 {
            answer = append(answer, 1)
			continue
        }
    
        i := 0
		num := n
        for num > 0 {
            remainder := num % 2
            if remainder == 0 {
				break
            }
            num /= 2
            i ++
        }
        answer = append(answer, n + int64(math.Pow(2, float64(i))) - int64(math.Pow(2, float64(i-1))))
    }

    return answer
}