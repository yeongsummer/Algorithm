package Programmers;

import java.util.Arrays;

public class table_hash_function {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data,(o1, o2) -> o1[col-1] != o2[col-1] ? o1[col-1]-o2[col-1] : o2[0]-o1[0]);
        for(int i = row_begin; i < row_end+1; i++){
            int sum = 0;
            for(int d : data[i-1]){
                sum += d % i;
            }
            answer = answer^sum;

        }
        return answer;
    }
}
