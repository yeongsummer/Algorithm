package Programmers;

public class prime_number_count {
    public int solution(int n, int k) {
        int answer = 0;
        Integer.toString(n, k);
        String num = convert(n, k) + "0";
        String tmp = "";
        for (int i = 0; i < num.length(); i ++){
            if (num.charAt(i) != '0'){
                tmp += num.charAt(i);
            } else {
                if (tmp.length() != 0){
                    if (is_prime_number(Integer.parseInt(tmp))){
                        answer += 1;
                    }
                    tmp = "";
                }
            }
        }
        return answer;
    }

    public String convert(int n, int k) {
        String result = "";
        int mod  = 0;
        while(n > 0){
            n = n / k;
            mod = n % k;
            result = Integer.toString(mod) + result;
        }
        return result;
    }

    public boolean is_prime_number(int x) {
        if(x == 1){
            return false;
        }
        for(int i = 2; i < Math.sqrt(x); i++){
            if(x%i == 0){
                return false;
            }
        }
        return true;
    }

}
