import java.util.Scanner;

public class Main {

    static int line3(int a, int b) {
        int one = b % 10;

        return a*one;
    }

    static int line4(int a, int b) {
        int ten = b / 10 % 10;

        return a*ten;
    }

    static int line5(int a, int b) {
        int hundred = b / 100;

        return a*hundred;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(line3(a,b));
        System.out.println(line4(a,b));
        System.out.println(line5(a,b));
        System.out.println(a*b);
    }
}
