import java.util.Scanner;

public class Main {
    static boolean Hansu(int n) {
        if(n == 1000) {
            return false;
        }
        int one = n % 10;
        int ten = n / 10 % 10;
        int hundred = n / 100;

        int dif1 = ten - one;
        int dif2 = hundred - ten;

        if(dif1 == dif2) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        if(N < 100) {
            System.out.println(N);
            return;
        }

        int count = 99;

        for(int i = 100; i <= N; i++) {
            if(Hansu(i)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
