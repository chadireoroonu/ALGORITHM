import java.util.Scanner;

public class Main {
	
	static int[] balls;
	static int N;
	static int M;
	static int S;
	static int E;
	static int num;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		int M = scan.nextInt();
		balls = new int[N];
			
		for (int i = 0; i < M; i++) {
			int S = scan.nextInt();
			int E = scan.nextInt();
			int num = scan.nextInt();
			for (int j = S-1; j < E; j++) {
				balls[j] = num;
			}
		}
			
		for (int k = 0; k < N; k++) {
			System.out.print(balls[k] + " ");
		}
	}
}