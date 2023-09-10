// 크기가 작은 문자열
package Programmers;

class Prg0118{
    public int solution(String t, String p) {
        long num = Long.parseLong(p);
        int answer = 0;

        for (int i=0;i<=t.length()-p.length();i++) {
            if (Long.parseLong(t.substring(i,i+p.length())) <= num) {
                answer += 1;
            }
        }
        
        return answer;
    }
}
