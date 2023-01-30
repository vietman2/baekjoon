import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int[] alphabet = new int[26];
        int max = 0;
        char result = '?';

        for(int i=0; i<line.length(); i++) {
            if(line.charAt(i) >= 'a' && line.charAt(i) <= 'z') {
                alphabet[line.charAt(i) - 'a']++;
            } else if(line.charAt(i) >= 'A' && line.charAt(i) <= 'Z') {
                alphabet[line.charAt(i) - 'A']++;
            }
        }

        for(int i=0; i<alphabet.length; i++) {
            if(alphabet[i] > max) {
                max = alphabet[i];
                result = (char)(i + 'A');
            } else if(alphabet[i] == max) {
                result = '?';
            }
        }

        System.out.println(result);
    }
}