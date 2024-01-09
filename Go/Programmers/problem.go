package programmers

import (
	"sort"
	"strconv"
	"strings"
)

func problems(plans [][]string) []string {
	answer := []string{}
	newPlan := []Plan{}
	for _, plan := range plans {
		hour := strings.Split(plan[1], ":")
		h, _ := strconv.Atoi(hour[0])
		m, _ := strconv.Atoi(hour[1])
		start := h*60 + m
		spend, _ := strconv.Atoi(plan[2])
		newPlan = append(newPlan, Plan{plan[0], start, spend})
	}

	sort.Slice(newPlan, func(i, j int) bool {
		return newPlan[i].startTime < newPlan[j].startTime
	})

	breakPlan := []Plan{}
	nowPlan := newPlan[0]
	now := newPlan[0].startTime + newPlan[0].spendTime
	i := 1
	for i < len(newPlan){
		if now <= newPlan[i].startTime {
			answer = append(answer, nowPlan.name)
			if now < newPlan[i].startTime && len(breakPlan) > 0 {
				nowPlan = breakPlan[len(breakPlan)-1]
				breakPlan = breakPlan[:len(breakPlan)-1]
				now = now + nowPlan.spendTime
				continue
			}
		} else {
			breakPlan = append(breakPlan, Plan{nowPlan.name, nowPlan.startTime, now - newPlan[i].startTime})
		}

		nowPlan = newPlan[i]
		now = nowPlan.startTime + nowPlan.spendTime
		i ++
	}

	answer = append(answer, nowPlan.name)
	for i := len(breakPlan)-1; i >= 0; i-- {
		answer = append(answer, breakPlan[i].name)
	}
	
	return answer
}

type Plan struct {
	name      string
	startTime int
	spendTime int
}