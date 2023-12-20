package programmers

import (
	"strconv"
	"strings"
)

func binary(s string) []int {
	i, zero_cnt := 0, 0

	for s != "1" {
		new_s := strings.ReplaceAll(s, "0", "")
		zero_cnt += len(s) - len(new_s)
		s = strconv.FormatInt(int64(len(new_s)), 2)
		i ++
	}

    return []int{i, zero_cnt}
}