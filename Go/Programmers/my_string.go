package programmers

func my_string(my_string string) string {
	stack := ""
	for _, s:= range my_string {
		add := string(s)
		for _, i := range stack {
			if s == i {
				add = ""
				break
			}
		}
		stack = stack + add
	}
    return stack
}