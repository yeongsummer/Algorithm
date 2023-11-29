package main

import (
	"container/heap"
)

func main() {
	fmt.Println(game(7,3,[]int{4, 2, 4, 5, 3, 3, 1}))
}

func game(n int, k int, enemy []int) int {
	hp := &IntHeap{}
	heap.Init(hp)
	i := 0

    for _, m := range enemy {
		fmt.Println(i, n, k, hp.Len())
		n -= m
		if n >= 0 {
			heap.Push(hp, m)
		} else if k > 0{
			k -= 1
			heap.Push(hp, m)
			n += heap.Pop(hp).(int)
		} else {
			break
		}
		i += 1
	}

    return i
}

func Max(a, b int) int {
    if a < b {
        return b
    } else if a > b {
        return a
    }
    return 0
}

type IntHeap []int

func (h IntHeap) Len() int {
    return len(h)
}

func (h IntHeap) Less(i, j int) bool {
    return h[i] > h[j] 
}

func (h IntHeap) Swap(i, j int) { 
    h[i], h[j] = h[j], h[i] 
} 

func (h *IntHeap) Push(elem interface{}) { 
    *h = append(*h, elem.(int)) 
} 

func (h *IntHeap) Pop() interface{} { 
    old := *h
	n := len(old)
	elem := old[n-1]
	*h = old[0 : n-1]
    return elem 
}