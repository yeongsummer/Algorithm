package Java.Programmers;

import java.util.Arrays;

public class book_time {
    public int solution(String[][] book_time) {
        int[] rooms = new int[24 * 60 + 10];
        for (String[] time : book_time) {
            rooms[changeMinute(time[0])] += 1 ;
            rooms[changeMinute(time[1]) + 10] -= 1 ;
        }

        for (int i = 1; i < rooms.length; i ++) {
            rooms[i] += rooms[i-1];
        }
        
        return Arrays.stream(rooms).max().getAsInt();
    }

    public int changeMinute(String time) {
        String[] times = time.split(":");
        return Integer.parseInt(times[0])*60 + Integer.parseInt(times[1]);
    }
}

