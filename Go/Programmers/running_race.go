package programmers

import "fmt"

func race(players []string, callings []string) []string {
	answer := make([]string, 0)
	ranking := []int{0,1,2,3,4}
	players_map := make(map[string]int)
	for i, p := range players{
		players_map[p] = i
	}
	for _, i := range callings {
		ranking[players_map[i]], ranking[players_map[i]-1] = ranking[players_map[i]-1], ranking[players_map[i]]
		fmt.Println(ranking)
	}

	for _, i := range ranking {
		answer = append(answer, players[i])
	}
    return answer
}