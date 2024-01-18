package main

import (
	"fmt"
)

func main() {
	fmt.Println(delivery(2, 7, []int{1, 0, 2, 0, 1, 0, 2}, []int{0, 2, 0, 1, 0, 2, 0}))
}

func delivery(cap int, n int, deliveries []int, pickups []int) int64 {
	answer := int64(0)
	deliveryCnt := 0
	pickupCnt := 0
	for i := n-1; i >= 0; i -- {
		if deliveries[i] != 0 || pickups[i] != 0 {
			cnt := 0
			for deliveryCnt < deliveries[i] || pickupCnt < pickups[i] {
				cnt ++
				deliveryCnt += cap
				pickupCnt += cap
			}
			deliveryCnt -= deliveries[i]
			pickupCnt -= pickups[i]
			answer += int64((i+1)*cnt*2)
		}
	}
	return answer
}