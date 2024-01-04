package programmers

import (
	"math"
)

func twoCircle(r1 int, r2 int) int64 {
	dot_cnt := int64(0)
    squar_r1, squar_r2 := math.Pow(float64(r1), 2), math.Pow(float64(r2), 2)
    for i := 1; i < r2; i ++ {
        a := math.Sqrt(squar_r2 - math.Pow(float64(i), 2))
        b := math.Sqrt(squar_r1 - math.Pow(float64(i), 2))
        if squar_r1 - math.Pow(float64(i), 2) < 0 {
            b = 0
        }
        a_int, _ := math.Modf(a)
        b_int, b_frac := math.Modf(b)
        dot_cnt += int64(a_int - b_int)
        if b_int != 0 && b_frac == 0 {
            dot_cnt += int64(1)
        }
    }

    return 4*(dot_cnt + int64(r2-r1+1))
}