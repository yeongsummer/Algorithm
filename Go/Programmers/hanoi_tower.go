package programmers

func hanoi(n int) (answer [][]int) {
    move(n, 1, 3, 2, &answer)
    return
}

func move(n, from, to, via int, route *[][]int) {
	if n == 1 {
	    *route = append(*route, []int{from, to})
	} else {
		move(n-1, from, via, to, route)
        *route = append(*route, []int{from, to})
		move(n-1, via, to, from, route)
    }
}