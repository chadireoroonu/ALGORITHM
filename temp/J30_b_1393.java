import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // 도착지의 x, y 좌표
        int ax = scan.nextInt();
        int ay = scan.nextInt();

        // 현재 기차의 x, y 좌표
        int tx = scan.nextInt();
        int ty = scan.nextInt();

        // 기차의 초당 x, y 좌표 증가분
        int dx = scan.nextInt();
        int dy = scan.nextInt();

        // 기차 직선의 기울기, 상수
        double ta = (double) dy/dx;
        double tb = ty - ta*tx;

        System.out.print("ta="+ta+" ");
        System.out.println("tb="+tb);

        // 기차와 직교하는 도착지 직선의 기울기, 상수
        double aa = (double) - dx/dy;
        double ab = ay - aa*ax;

        System.out.print("aa="+aa+" ");
        System.out.println("ab="+ab);

        // 뛰어내릴 좌표
        int x = (int) - ((tb-ab)*1/(ta-aa));
        int y = (int) (ta*x + tb);
        System.out.print(x+" "+y);
    }
}