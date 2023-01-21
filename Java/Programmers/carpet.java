package Java.Programmers;

public class carpet {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int[] answer = s.solution(12, 4);
        System.out.println(answer);
    }
}

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown+yellow;
        
        for(int i = 1; i < Math.sqrt(total)+1; i++) {
            int j = total / i;
            
            if ((i-2)*(j-2) == yellow) {
                answer[0] = j;
                answer[1] = i;
                break;
            }
        }
        return answer;
    }
}