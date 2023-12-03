package programmers

func solution(arrayA []int, arrayB []int) int {
    divisorA := findGcd_N(arrayA)
	divisorB := findGcd_N(arrayB)

	if divisorA != 1 {
		for _, n := range arrayA {
			if n % divisorB == 0 {
				divisorB = 0
				break
			}
		}
	} else {
		divisorA = 0
	}

	if divisorB != 1 {
		for _, n := range arrayB {
			if n % divisorA == 0 {
				divisorA = 0
				break
			}
		}
	} else {
		divisorB = 0
	}

    return max(divisorA, divisorB)
}

func findGcd_N(arr []int) int {
	gcd := arr[0]
	for _, n := range arr {
		gcd = findGcd(gcd, n)
	}
	return gcd
}

func findGcd(a, b int) int {
	for b > 0 {
		a, b = b, a % b
	}
	return a
}

func max(a,b int) int {
	if a > b {
		return a
	}

	return b
}