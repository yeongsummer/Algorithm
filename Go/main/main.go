package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(tictacto([]string{"O.X", ".O.", "..X"}))
}

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
		if strings.Count(col, "O") == 3 {
			bingoO ++
		}
		if strings.Count(col, "X") == 3 {
			bingoX ++
		}
	}

	dia1, dia2 := "", ""
	for i:=0; i<3; i++ {
		dia1 += strings.Split(board[i], "")[i]
		dia2 += strings.Split(board[i], "")[2-i]
	}
	
	if strings.Count(dia1, "O") == 3 {
		bingoO ++
	}
	if strings.Count(dia1, "X") == 3 {
		bingoX ++
	}
	if strings.Count(dia2, "O") == 3 {
		bingoO ++
	}
	if strings.Count(dia2, "X") == 3 {
		bingoX ++
	}



	if bingoO == 0 && bingoX == 0 {
		if countO == countX || countO == countX+1 {
			return 1
		}
	} else if bingoO == 1 && bingoX == 0 {
		if countO - 1 == countX {
			return 1
		}
	} else if bingoO == 0 && bingoX == 1 {
		if countO  == countX {
			return 1
		}
	}

    return 0
}
