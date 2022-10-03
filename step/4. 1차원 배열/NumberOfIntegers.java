import java.util.Scanner;
import java.lang.String;

public class NumberOfIntegers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int zero = 0;
        int one = 0;
        int two = 0;
        int three = 0;
        int four = 0;
        int five = 0;
        int six = 0;
        int seven = 0;
        int eight = 0;
        int nine = 0;

        long product = a*b*c;

        while(true) {
            int rem = (int) (product % 10);
            product /= 10;

            if(rem == 0){
                zero++;
            }
            else if(rem == 1) {
                one++;
            }
            else if(rem == 2) {
                two++;
            }
            else if(rem == 3) {
                three++;
            }
            else if(rem == 4) {
                four++;
            }
            else if(rem == 5) {
                five++;
            }
            else if(rem == 6) {
                six++;
            }
            else if(rem == 7) {
                seven++;
            }
            else if(rem == 8) {
                eight++;
            }
            else if(rem == 9) {
                nine++;
            }

            if(product == 0) {
                break;
            }
        }

        System.out.println(zero);
        System.out.println(one);
        System.out.println(two);
        System.out.println(three);
        System.out.println(four);
        System.out.println(five);
        System.out.println(six);
        System.out.println(seven);
        System.out.println(eight);
        System.out.println(nine);
    }
}
