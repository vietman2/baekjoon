import java.util.Scanner;

public class AdditionCycle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        int ten = x / 10;
        final int ten_answer = ten;
        int one = x % 10;
        final int one_answer = one;

        int count = 0;

        while(true) {
            int sum = ten + one;

            ten = one;
            one = sum % 10;

            count++;

            if(ten == ten_answer && one == one_answer) {
                System.out.println(count);
                break;
            }
        }
    }
}
