package main

import (
	"fmt"
)

func main() {
	fmt.Println(long_jump(4))
}

func long_jump(n int) int64 {
    memo := make([]int, 2001)
	memo[1] = 1
	memo[2] = 2
	for i := 3; i <= n; i ++ {
		memo[i] = memo[i-1] + memo[i-2]
	}
    return int64(memo[n]%1234567)
}