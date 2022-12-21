import java.util.Scanner;

public class Calculator {
    static int addition(int a, int b) {
        return a+b;
    }

    static int subtraction(int a, int b) {
        return a-b;
    }

    static int multiplication(int a, int b) {
        return a*b;
    }

    static int division(int a, int b) {
        return a/b;
    }

    static int remainder(int a, int b) {
        return a%b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(addition(a, b));
        System.out.println(subtraction(a, b));
        System.out.println(multiplication(a, b));
        System.out.println(division(a, b));
        System.out.println(remainder(a, b));
    }

}
