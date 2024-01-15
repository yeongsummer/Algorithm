package programmers

import "sort"

func intercept(targets [][]int) int {
	answer := 1
	sort.Slice(targets, sortTarget(targets))
	end := targets[0][1]
    for _, t := range targets[1:] {
		if t[0] >= end {
            end = t[1]
			answer += 1
        } else {
            if t[1] < end {
                end = t[1]
            }
        }
	}
    return answer
}

func sortTarget(targets [][]int) func(i, j int) bool {
	return func(i, j int) bool {
		if targets[i][0] < targets[j][0] {
			return true
		} else if targets[i][0] > targets[j][0] {
			return false
		}

		return targets[i][1] < targets[j][1]
	}
}