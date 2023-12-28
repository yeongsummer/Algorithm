package programmers

func array_cut(n int, left int64, right int64) []int {
	result := []int{}
	for i:=int(left); i<=int(right); i++ {
		q, r := (i+1)/n, (i+1)%n
		if r == 0 {
			result = append(result, n)
		} else {
			if r <= q+1 {
				result = append(result, q + 1)
			} else {
				result = append(result, r)
			}
		}
	}
    return result
}