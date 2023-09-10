package Programmers;

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class PlayingAlone {
    public int solution(int[] cards) {
        List<Integer> answer = new ArrayList<Integer>();
        int[] opened = new int[cards.length];
        for (int i = 0; i < cards.length; i ++) {
            if (opened[i] != 1) {
                int cnt = 0;
                int next = cards[i] - 1;
                while (opened[next] != 1) {
                    cnt += 1;
                    opened[next] = 1;
                    next = cards[next] - 1;
                }
                answer.add(cnt);
             }
        }
        
        if (answer.size() == 1) {
            return 0;
        } else {
            Collections.sort(answer, Collections.reverseOrder());
        }

        return answer.get(0)*answer.get(1);
    }
}


