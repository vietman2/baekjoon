import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int numbers[] = new int[N];
        int min = 1000000;
        int max = -1000000;

        for(int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();

            if(numbers[i] < min) {
                min = numbers[i];
            }
            if(numbers[i] > max) {
                max = numbers[i];
            }
        }

        System.out.println(min + " " + max);

    }
}
