import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++) {
            String line = br.readLine();

            String values[] = line.split("\\s");
            int a = Integer.parseInt(values[0]);
            int b = Integer.parseInt(values[1]);

            int sum = a + b;
            if (i != 0) {
                bw.newLine();
            }
            bw.write(String.valueOf(sum));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
