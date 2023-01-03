import java.util.Scanner;

public class Main {
    static int first(int a, int b, int c) {
        return (a+b)%c;
    }

    static int second(int a, int b, int c) {
        return (a*b)%c;
    }

    static int third(int a, int b, int c) {
        return ((a%c) + (b%c))%c;
    }

    static int forth(int a, int b, int c) {
        return ((a%c) * (b%c))%c;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(first(a, b, c));
        System.out.println(third(a,b,c));
        System.out.println(second(a,b,c));
        System.out.println(forth(a,b,c));
    }
}
