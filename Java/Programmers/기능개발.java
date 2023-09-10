package Programmers;
import java.util.*;

class Develop {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> ans = new ArrayList<>();
        Deque<Integer> p = new ArrayDeque<>();
        Deque<Integer> s = new ArrayDeque<>();

        for (int i = 0; i < progresses.length; i++) {
            p.offer(progresses[i]);
            s.offer(speeds[i]);
        }

        int n = 1;
        while (p.size() > 0) {
            int cnt = 0;
            while (p.size() > 0) {
                if (p.getFirst() + s.getFirst()*n >= 100) {
                    p.pollFirst();
                    s.pollFirst();
                    cnt++;
                    if (p.size() == 0) {
                        ans.add(cnt);
                    }
                } else {
                    if (cnt > 0) {
                        ans.add(cnt);
                    }
                    break;
                }
            } 
            n++;
        }
        int[] answer = new int[ans.size()];

        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }

        return answer;
    }
}