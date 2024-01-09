package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(problems([][]string{
		{"a", "09:00", "10"}, {"b", "09:10", "10"}, {"c", "09:15", "10"}, {"d", "09:30", "10"}, {"e", "09:35", "10"}}))
}

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
	fmt.Println(newPlan)
	breakPlan := []Plan{}
	nowPlan := newPlan[0]
	now := newPlan[0].startTime + newPlan[0].spendTime
	i := 1
	for i < len(newPlan){
		fmt.Println(i, now, nowPlan, breakPlan, answer)
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
