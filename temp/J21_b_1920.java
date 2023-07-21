import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = scan.nextInt();
        }

        int M = scan.nextInt();
        for (int j = 0; j < M; j++) {
            int flag = 0;
            int temp = scan.nextInt();
            for (int k = 0; k < N; k++) {
                if (A[k] == temp) {
                    flag = 1;
                }
            }
            System.out.println(flag);
        }
    }
}