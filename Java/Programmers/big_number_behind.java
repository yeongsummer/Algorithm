package Programmers;

import java.util.Arrays;
import java.util.Stack;

public class big_number_behind {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < numbers.length; i++){
            while (!stack.empty() && numbers[stack.elementAt(stack.size())] < numbers[i]) {
                answer[stack.pop()] = numbers[i];
            }
            stack.push(i);
        }
        return answer;
    }
}
