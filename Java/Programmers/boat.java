package Java.Programmers;

import java.util.Arrays;

public class boat {
    public static void main(String[] args) throws Exception {
    }
}
    
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int i = 0;
        int j = people.length-1;
        for (; i <= j; j--) {
            if (i == j) {
                answer++;
                break;
            }
            if (people[i] + people[j] <= limit) {
                i++;
            }
            answer++;
        }
    
        return answer;
    }
}