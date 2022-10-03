import java.util.Scanner;

public class OXQuiz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.valueOf(sc.nextLine());

        for(int i = 0; i < N; i++) {
            String quiz = sc.nextLine();
            int score = 0;
            int consecutive = 0;

            for(int j = 0; j < quiz.length(); j++) {
                if(quiz.charAt(j) == 'O') {
                    consecutive++;
                    score += consecutive;
                }
                else {
                    consecutive = 0;
                }
            }

            System.out.println(score);
        }


    }
}
