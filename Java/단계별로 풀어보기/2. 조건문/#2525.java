import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int add = sc.nextInt();

        int out_minute = minute + add;
        int add_hour = out_minute / 60;

        if(out_minute >= 60) {
            out_minute %= 60;
            hour += add_hour;
        }

        if(hour >= 24) {
            hour -= 24;
        }

        System.out.println(hour + " " + out_minute);
    }
}
