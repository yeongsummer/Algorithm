// 크기가 작은 문자열
package Java.Programmers;

public class prg0118{
    public static void main(String[] args) throws Exception {
        int answer = solution("4324", "66");
        System.out.println(answer);
    }

    public static int solution(String t, String p) {
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

