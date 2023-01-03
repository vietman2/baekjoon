import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int C = sc.nextInt();

        for(int i = 0; i < C; i++) {
            int N = sc.nextInt();
            double scores[] = new double[N];
            double total = 0;

            for(int j = 0; j < N; j++) {
                double score = sc.nextInt();
                scores[j] = score;
                total += score;
            }

            double average = total / N;
            int count = 0;

            for(int k = 0; k < N; k++) {
                if(scores[k] > average) {
                    count++;
                }
            }

            double ratio = (double) count / N * 100;

            System.out.println(String.format("%.3f", ratio) + "%");
        }
    }
}
