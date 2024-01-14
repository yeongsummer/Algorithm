package programmers

func solution(users [][]int, emoticons []int) []int {
    answer := []int{0, 0}
    for _, p := range generatePermutations([]int{10, 20, 30, 40}, len(emoticons), make([]int, len(emoticons))) {
        peoples, sales := 0, 0
        for _, u := range users {
            price := 0
            for i, s := range p {
                if s >= u[0] {
                    price += emoticons[i]-emoticons[i]*s/100
                }
            }
            if price >= u[1] {
                peoples += 1
            } else {
                sales += price
            }
        }
        if peoples > answer[0] || (peoples == answer[0] && sales > answer[1]) {
            answer[0], answer[1] = peoples, sales
        }
    }
    return answer
}

func generatePermutations(input []int, length int, result []int) [][]int {
    var permutations [][]int

    if length == 0 {
        permutation := make([]int, len(result))
        copy(permutation, result)
        permutations = append(permutations, permutation)
        return permutations
    }

    for i := 0; i < len(input); i++ {
        result[len(result)-length] = input[i]
        permutations = append(permutations, generatePermutations(input, length-1, result)...)
    }

    return permutations
}
