import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        int words = 0;

        for(int i=0; i<line.length(); i++) {
            if(line.charAt(i) == ' ') {
                words++;
            }
        }

        if(line.charAt(0) == ' ') {
            words--;
        }

        if(line.charAt(line.length()-1) == ' ') {
            words--;
        }

        System.out.println(words+1);
    }
}