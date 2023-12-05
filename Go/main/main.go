package main

import (
	"fmt"
)

func main() {
	fmt.Println(tournament(256,127,255))
}

func tournament(n int, a int, b int) int {
	answer := 1
    if a > b {
        a, b = b, a
    }
	for a%2 != 1 || b%2 != 0 || a+1 == b {
		answer += 1
		a = a/2 + a%2
		b = b/2 + b%2
	}
	return answer
}


// func findRound(n int, a int, b int) int {
// 	fmt.Println("start", a,b, n)
//     for i := int(math.Sqrt(float64(n))); i >= 0; i -- {
// 		fmt.Println("i", i)
// 		m := int(math.Pow(2, float64(i)))
// 		if b > m {
// 			fmt.Println(i, m)
// 			if a <= m {
// 				return i+1
// 			} else {
// 				return findRound(m, a - m, b - m)
// 			}
// 		}
// 	}
// 	return -1
// }
