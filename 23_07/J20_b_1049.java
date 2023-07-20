import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        // 6개, 1개 최소값
        int mini_six = N*N*N;
        int mini_one = N*N*N;

        // 판매단위별 최소값 저장
        for (int i = 0; i < M; i++) {
            int six = scan.nextInt();
            if (six < mini_six) {
                mini_six = six;
            }
            int one = scan.nextInt();
            if (one < mini_one) {
                mini_one = one;
            }
        }
        // 한 개씩 살때가 더 쌀 경우
        if (mini_one*6 < mini_six) {
            System.out.println(mini_one*N);
        }
        // 여섯개 묶음이 더 쌀 경우
        else {
            // 줄 개수 맞춰 사는게 더 쌀 경우
            if (N/6*mini_six+N%6*mini_one < (N/6+1)*mini_six)
            System.out.println(N/6*mini_six+N%6*mini_one);
            // 줄 개수 남기는게 더 쌀 경우
            else {
                System.out.println((N/6+1)*mini_six);
            }
        }
    }
}