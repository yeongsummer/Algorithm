package Programmers;
class Solution {
    static int[][] matrix;
    static int minNum;
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        matrix = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = (i) * columns + j+1;
          }
        }

        for (int i = 0; i < queries.length; i++) {
            int x1 = queries[i][0]-1;
            int y1 = queries[i][1]-1;
            int x2 = queries[i][2]-1;
            int y2 = queries[i][3]-1;
            int n = matrix[x1][y1];
            minNum = n;
            int x = x1;
            int y = y1;
            while (y < y2) {
                y++;
                n = change(x, y, n);
            }
            while (x < x2) {
                x++;
                n = change(x, y, n);
            }
            while (y > y1) {
                y--;
                n = change(x, y, n);
            }
            while (x > x1) {
                x--;
                n = change(x, y, n);
            }
            answer[i] = minNum;
        }

        return answer;
        }

    static int change(int x, int y, int n) {
        int temp = matrix[x][y];
        matrix[x][y] = n;
        minNum = Math.min(minNum, temp);

        return temp;
    }
}