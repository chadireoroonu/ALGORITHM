import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sacn = new Scanner(System.in);

        int N = sacn.nextInt();
        int[] array = new int(N);

        for (int i = 0; i < N; i++) {
            int order = sacn.nextInt();
            int temp = 0;
            for (int j = 0; j < N; j++) {
                if (order == temp) {
                    array[j] = i;
                    break
                }
                if (array[j] == 0) {
                    temp += 1
                }
            }
        }
        for (int k = 0; k < N; k++) {
            System.out.println(array[k])
        }
    }
}