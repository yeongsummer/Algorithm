package programmers

import (
	"fmt"
	"strings"
)

func tictacto(board []string) int {
	countO, countX := 0, 0
	bingoO, bingoX := 0, 0
	for _, row := range board {
		cntO := strings.Count(row, "O")
		if cntO == 3 {
			bingoO ++
		}
		countO += cntO
		cntX := strings.Count(row, "X")
		if cntX == 3 {
			bingoX ++
		}
		countX += cntX
	}

	for i:=0; i<3; i++ {
		col := ""
		for j:=0; j<3; j++ {
			col += strings.Split(board[j], "")[i]
		}
		fmt.Println(col)
		if strings.Count(col, "O") == 3 {
			bingoO ++
		}
		if strings.Count(col, "X") == 3 {
			bingoX ++
		}
	}

	if strings.Count(strings.Split(board[0], "")[0] + strings.Split(board[1], "")[1] + strings.Split(board[2], "")[2], "O") == 3 {
		bingoO ++
	}
	if strings.Count(strings.Split(board[0], "")[2] + strings.Split(board[1], "")[1] + strings.Split(board[2], "")[0], "X") == 3 {
		bingoX ++
	}


    return -1
}

