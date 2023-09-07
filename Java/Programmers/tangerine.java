package Programmers;

import java.util.*;

public class tangerine {
    public static void main(String[] args) throws Exception {
    }
}

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer,Integer> map =new HashMap<>();

        for (int t : tangerine) {
            map.put(t, map.getOrDefault(t, 0) + 1);
        }

        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((o1, o2) -> map.get(o2)-map.get(o1));

        for (Integer key:list) {
            k -= map.get(key);
            answer++;
            
            if (k <= 0) {
                break;
            }
        }

        return answer;
    }
}

class Solution1 {
    public int solution(int[][] triangle) {
        int answer = 0;
        for (int i=1; i<triangle.length; i++) {
            for (int j = 0; j<triangle[i].length; j++) {
                if (i == 0) {
                    triangle[i][j] += triangle[i-1][j];
                } else if (j == triangle.length - 1) {
                    triangle[i][j] += triangle[i-1][j-1];
                } else {
                    triangle[i][j] += Math.max(triangle[i-1][j], triangle[i-1][j-1]);
                }
            }
        }
        return answer;
    }
}