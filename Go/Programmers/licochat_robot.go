package programmers

func robot(board []string) int {
	r_i, r_j := findCoordinate(board)
	d := bfs(board, []int{r_i, r_j})
    return d
}

func findCoordinate(board []string) (r_i, r_j int) {
	for i := 0; i < len(board); i++ {
		for j :=  0; j <  len(board[i]); j++ {
			if board[i][j] == 'R' {
				r_i, r_j = i, j
				break
			}
		}
	}
	return r_i, r_j
}

func bfs(board []string, start []int) int {
	dxy := [][]int{{1,0},{0,1},{-1,0},{0,-1}}
	n, m := len(board), len(board[0])
	deq := deque{}
	deq.push(start)
	var visited [][]int
    for i := 0; i < len(board); i++ {
        visited = append(visited, make([]int, len(board[0])))
    }
	visited[start[0]][start[1]] = 1

	for !deq.empty() {
		x, y := deq.popFirst()
		if board[x][y] == 'G' {
			return visited[x][y] - 1
		}

        for i := 0; i < 4; i++ {
			now_x, now_y := x, y
			for true {
				next_x, next_y := now_x + dxy[i][0], now_y + dxy[i][1]
				if next_x > -1 && next_x < n && next_y > -1 && next_y < m && board[next_x][next_y] != 'D' {
					now_x, now_y = next_x, next_y
				} else {
					break
				}
			}
			if visited[now_x][now_y] == 0 {
				visited[now_x][now_y] = visited[x][y] + 1
				deq.push([]int{now_x, now_y})
			}
		}
	}
	return -1
}


type deque struct {
	indexes [][]int
}

func (d *deque) push(i []int) {
	d.indexes = append(d.indexes, i)
}

func (d *deque) popFirst() (int, int) {
	i, j := d.indexes[0][0], d.indexes[0][1]
	d.indexes = d.indexes[1:]
	return i, j
}

func (d *deque) popLast() (int, int) {
	i, j := d.indexes[len(d.indexes)-1][0], d.indexes[len(d.indexes)-1][1]
	d.indexes = d.indexes[:len(d.indexes)-1]
	return i, j
}

func (d *deque) empty() bool {
	return 0 == len(d.indexes)
}