package programmers

func queue_sum(queue1 []int, queue2 []int) int {
	queue := append(queue1, append(queue2, queue1...)...)
	total_sum := 0
	for _, n := range append(queue1, queue2...) {
			total_sum += n
	}
	interval_sum, target_sum := 0, total_sum/2
	start, end := 0, 0
	l := len(queue)
	
	for start = 0; start <l; start++ {
		for interval_sum < target_sum && end < l {
			interval_sum += queue[end]
			end += 1
		}

		if interval_sum == target_sum {
			break
		}
		interval_sum -= queue[end]
	}
		
    return start
}