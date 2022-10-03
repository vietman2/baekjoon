import java.util.Scanner;

public class Average {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        double scores[] = new double[N];
        double max = -1;

        for(int i = 0; i < N; i++) {
            double number = sc.nextInt();
            scores[i] = number;
            if(number > max) {
                max = number;
            }
        }

        double SumNewScores = 0.0;

        for(int i = 0; i < N; i++) {
            double NewScore = scores[i] / max;
            SumNewScores += NewScore;
        }

        double NewAverage = (SumNewScores / N) * 100;

        System.out.println(NewAverage);
    }
}
