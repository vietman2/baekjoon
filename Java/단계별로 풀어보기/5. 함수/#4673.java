public class Main {
    static int d(int n) {
        int number = n;

        while(true) {
            number += n % 10;
            n /= 10;

            if(n == 0) {
                break;
            }
        }

        return number;
    }

    public static void main(String[] args) {
        boolean numbers[] = new boolean[10000];

        int startPoint = 0;
        for(int i = 1; i <= 10000; i++) {

            if(numbers[i-1] == false) {
                startPoint = i;
            }
            else {
                continue;
            }

            int number = startPoint;

            while(true) {
                int result = d(number);
                if(result > 10000) {
                    break;
                }

                numbers[result-1] = true;
                number = result;
            }
        }


        for(int i = 0; i < 10000; i++) {
            if(numbers[i] == false) {
                System.out.println(i+1);
            }
        }

    }
}
