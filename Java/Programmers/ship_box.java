package Programmers;

import java.util.Stack;

public class ship_box {
    public int solution(int[] order) {
        Stack<Integer> stack = new Stack<>();
        int box = 1;
        int target_idx = 0;

        while (target_idx < order.length){
            if (order[target_idx] ==  box){
                target_idx ++;
                box ++;
            } else if (stack.size() > 0 && order[target_idx] == stack.peek()){
                target_idx ++;
                stack.pop();
            } else if (box < order.length){
                stack.add(box);
                box ++;
            } else {
                break;
            }
        }
        return target_idx;
    }
}
