package Programmers;

class RollCake {
    public int solution(int[] topping) {
        int answer = 0;
        int[] front_cnt = new int[10001];
        int[] back_cnt = new int[10001];
        int front_total = 0;
        int back_total = 0;

        for (int t : topping) {
            if (back_cnt[t] == 0) {
                back_total += 1;
            }
            back_cnt[t] += 1;
        }

        for (int t : topping) {
            if (front_cnt[t] == 0) {
                front_total += 1;
            }

            front_cnt[t] += 1;
            back_cnt[t] -= 1;

            if (back_cnt[t] == 0) {
                back_total -= 1;
            }

            if (front_total == back_total) {
                answer += 1;
            } else if (front_total > back_total) {
                break;
            }
        }
        
        return answer;
    }
}