package programmers

import (
	"strconv"
	"strings"
)

func bookTime(book_time [][]string) int {
	var answer int
	rooms := make([]int, 24*60+10)
	for _, time := range book_time {
		rooms[changeMinute(time[0])] += 1
		rooms[changeMinute(time[1])+10] -= 1
	}

	for i := 1; i < len(rooms); i++ {
		rooms[i] += rooms[i-1]
	}

	for _, room := range rooms {
		if answer < room {
			answer = room
		}
	}
    return answer
}

func changeMinute(time string) int {
	times := strings.Split(time, ":")
	h, _ := strconv.Atoi(times[0])
	m, _ := strconv.Atoi(times[1])
	return h + m
}