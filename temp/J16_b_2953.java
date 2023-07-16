import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int winner = 0;
        int score = 0;

        for (int i = 1; i <= 5; i++) {
            int point = 0;
            for (int j = 0; j < 4; j++) {
                point += scan.nextInt();
            }
            // 최고점 참가자 재할당
            if (point > score){
                winner = i;
                score = point;
            }
        }
        System.out.println(winner+" "+score);
    }
}