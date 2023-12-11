import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int maxi = 0;
		
		for (int i = 0; i < N; i++) {
			int M = scan.nextInt();
			if (M > maxi) {
				maxi = M;
			}
		}
		System.out.println(maxi);
	}
}