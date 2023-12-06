package programmers

func long_jump(n int) int64 {
    memo := make([]int64, 2001)
    memo[1] = 1%1234567
    memo[2] = 2%1234567
    for i := 3; i <= n; i ++ {
        memo[i] = (memo[i-1] + memo[i-2])%1234567
    }
    return memo[n]
}