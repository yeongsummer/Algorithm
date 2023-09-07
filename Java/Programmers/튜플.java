package Programmers;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Solution {
    public int[] solution(String s) {
        String[] arr = s.substring(2, s.length() - 2).split(",|\\},\\{");
        HashMap<Integer,Integer> hashMap = new HashMap<Integer,Integer>();

        for (String i:arr) {
            int j = Integer.parseInt(i);
            if (hashMap.containsKey(j)) {
                hashMap.put(j, hashMap.get(j)+1);
            } else {
                hashMap.put(j, 1);
            }
        }
        
        List<Integer> numberList = new ArrayList<Integer>(hashMap.keySet());
        Collections.sort(numberList, (v1, v2) -> (hashMap.get(v2) - hashMap.get(v1)));
 
        int[] answer = new int[numberList.size()];
        for (int i = 0; i < numberList.size(); i++)
            answer[i] = numberList.get(i);
        return answer;
    }
}