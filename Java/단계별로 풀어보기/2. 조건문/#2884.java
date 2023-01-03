import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int in_hour = sc.nextInt();
        int in_minute = sc.nextInt();

        int out_hour = in_hour;
        int out_minute = in_minute;

        boolean minute = false;

        if(in_minute >= 45) {
            out_minute -= 45;
        }
        else {
            int remainder = 45 - in_minute;
            out_minute = 60 - remainder;
            minute = true;
        }

        if(minute == true) {
            if(in_hour != 0) {
                out_hour--;
            }
            else {
                out_hour = 23;
            }
        }

        System.out.println(out_hour + " " + out_minute);
    }
}
