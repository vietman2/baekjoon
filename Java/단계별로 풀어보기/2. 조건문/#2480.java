import java.util.Scanner;

public class Main {
    static int max(int a, int b, int c) {
        int max = a;

        if(b > max) {
            max = b;
        }

        if(c > max) {
            max = c;
        }

        return max;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if(a != b && a != c && b != c) {
            System.out.println(max(a,b,c) * 100);
        }
        else if(a == b && a == c) {
            int prize = 10000 + (a * 1000);
            System.out.println(prize);
        }
        else {
            if(a == b) {
                int prize = 1000 + a*100;
                System.out.println(prize);
            }
            else if(a == c) {
                int prize = 1000 + a*100;
                System.out.println(prize);
            }
            else {
                int prize = 1000 + b*100;
                System.out.println(prize);
            }
        }
    }
}
