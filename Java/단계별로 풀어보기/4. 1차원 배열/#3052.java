import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int remainders[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
        int number = 0;

        for(int i = 0; i < 10; i++) {
            int remainder = sc.nextInt() % 42;
            boolean already = false;

            for(int value : remainders) {
                if(value == remainder) {
                    already = true;
                    break;
                }
            }

            if(already == false) {
                remainders[number] = remainder;
                number++;
            }
        }

        System.out.println(number);
    }
}
