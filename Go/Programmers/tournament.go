package programmers

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
