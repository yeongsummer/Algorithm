package programmers

import (
	"math"
)

func mineral(picks []int, minerals []string) int {
	answer := 1250
	num := 0
	for _, p := range picks {
		num += p
	}
	dfs(0, picks, minerals, &answer, num)
    return answer
}

func dfs(stress int, picks []int, minerals []string, ans *int, num int) {
	if stress >= *ans {
		return
	}
	if num == 0 || len(minerals) == 0 {
		if stress < *ans {
			*ans = stress
		}
		return
	}

	for i, n := range picks {
		if n != 0 {
			add := 0
			j := 0
			for ;j<5; j++ {
				if j >= len(minerals) {
					break
				}
				add += calStress(i, minerals[j])
			}
			picks[i] -= 1
			dfs(stress+add, picks, minerals[j:], ans, num-1)
			picks[i] += 1
		}
	}
}

func calStress(pick int, mineral string) int {
	if mineral == "diamond" {
		return int(math.Pow(5, float64(pick)))
	} else if mineral == "iron" && pick == 2{
		return 5
	}
	return 1
}