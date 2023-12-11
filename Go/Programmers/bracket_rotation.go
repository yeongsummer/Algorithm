package programmers


func checkBracket(s string) int {
	answer := 0
	bracket_map := map[string]string{")":"(", "}":"{", "]":"["}
	l := len(s)

	for start := 0; start < l; start ++ {
		bracket_list := []string{}
		for i := start; i < start+l; i ++ {
			b := string(s[i%l])
			if b == "(" || b == "{" || b == "[" {
				bracket_list = append(bracket_list, b)
			} else {
				if len(bracket_list) == 0 || bracket_list[len(bracket_list)-1] != bracket_map[b]{
					bracket_list = append(bracket_list, b)
					break
				} else {
					bracket_list = bracket_list[:len(bracket_list)-1]
				}
			}
		}
		if len(bracket_list) == 0 {
			answer += 1
		}
	}
	return answer
}