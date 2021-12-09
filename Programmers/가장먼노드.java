import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        ArrayList<ArrayList<Integer>> graph=new ArrayList<ArrayList<Integer>>();
        for(int i=0;i<edge.length;i++){
            graph.add(new ArrayList<Integer>());
        }

        for(int[] node:edge){
            graph.get(node[0]).add(node[1]);
            graph.get(node[1]).add(node[0]);
        }
        
        int[] minDists = new int[n+1];
        minDists[1] = 1;
        Queue<Integer> q=new LinkedList<>();
        q.add(1);
        while (!q.isEmpty()) {
            int m = q.poll();
            for(int v:graph.get(m)){
                if(minDists[v] == 0){
                    minDists[v]=minDists[m]+1;
                    q.add(v);
                }
            }
        }
        int answer = 0;
        int max_dist = 0;
        for(int d:minDists){
            if (max_dist<d) {
                max_dist=d;
                answer = 1;
            } else {
                if (max_dist==d) {
                    answer++;
                }
            }
        }

        return answer;
    }
}