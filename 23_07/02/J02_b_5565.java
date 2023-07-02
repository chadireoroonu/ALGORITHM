package month07;

import java.util.Scanner;

public class J02_b_5565 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int total = scan.nextInt();
		
		for (int i = 0; i < 9; i++) {
			total -= scan.nextInt();
		}
		
		System.out.println(total);
	}
}
