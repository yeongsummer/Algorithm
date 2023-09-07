package Programmers;

import java.util.*;

public class maze_escape {
    public static void main(String[] args) throws Exception {
        Maze m = new Maze();
        String[] lst = {"SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"};
        int answer = m.solution(lst);
        System.out.println(answer);
    }
}

class Maze {
    static int[][] visited_1, visited_2;
    static char[][] map;
    static int dx[] = {-1, 1, 0, 0};
    static int dy[] = {0, 0, -1, 1};
    public int solution(String[] maps) {
        int s_x = 0, s_y = 0, e_x = 0, e_y = 0, l_x = 0, l_y = 0;
        map = new char[maps.length][maps[0].length()];
        visited_1 = new int[maps.length][maps[0].length()];
        visited_2 = new int[maps.length][maps[0].length()];

        for(int i=0;i<maps.length;i++){
            map[i] = maps[i].toCharArray();
        }

        for (int i = 0; i < map.length; i++) {
            for(int j = 0;j < map[i].length; j++) {
                if (map[i][j] == 'S') {
                    s_x = i;
                    s_y = j;
                } else if (map[i][j] == 'E') {
                    e_x = i;
                    e_y = j;
                } else if (map[i][j] == 'L') {
                    l_x = i;
                    l_y = j;
                }
            }
        }
        
        int ans_1 = bfs(s_x, s_y, l_x, l_y, visited_1);
        int ans_2 =  bfs(l_x, l_y, e_x, e_y, visited_2);
        if (ans_1 == -1 || ans_2 == -1) {
            return -1;
        }

        return ans_1 + ans_2;
    }

    public static int bfs(int x, int y, int end_x, int end_y, int[][] visited) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(x, y));
        visited[x][y] = 1;

        while(!q.isEmpty()) {
            Node node = q.poll();
            x = node.getX();
            y = node.getY();
            if (x == end_x && y == end_y) {
                return visited[x][y] - 1;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= map.length || ny < 0 || ny >= map[0].length) continue;
              
                if (visited[nx][ny] == 0 && map[nx][ny] != 'X') {
                    visited[nx][ny] = visited[x][y] + 1;
                    q.offer(new Node(nx, ny));
                }
            }
        }

        return -1;
    }
}          

class Node {
    private int x;
    private int y;
    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }
}