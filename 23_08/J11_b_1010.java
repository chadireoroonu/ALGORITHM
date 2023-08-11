import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        long result;
        int T = scan.nextInt();
        for (int i = 0; i < T; i++) {
            int N = scan.nextInt();
            int M = scan.nextInt();

            result = 1;
            // for (int j = 0; j < N; j++) {
            for (int j = 1; j <= N; j++) {
                // result = result * (M - j) / (j + 1);
                result = result * (M - j + 1) / j;
                // result *= (M - j + 1) / j;
                // result *= (M - j) / (j + 1);
            }
            System.out.println(result);
        }
    }
}