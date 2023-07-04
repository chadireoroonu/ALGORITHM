package month07;

import java.util.Scanner;

public class J04_b_10156 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int K = scan.nextInt();
		int N = scan.nextInt();
		int M = scan.nextInt();
		scan.close();
		
		if (K * N - M > 0) {
			System.out.println(K * N - M);
		}
		else {
			System.out.println(0);
		}
	}
}
