package day06261;

import java.util.*;

public class J28_b_5086 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int a = scan.nextInt();
		int b = scan.nextInt();
		
		// a, b가 0이 아니라면 반복
		while (a != 0 && b != 0) {
			if (b % a == 0) {
				System.out.println("factor");
			}
			else if (a % b == 0) {
				System.out.println("multiple");
			}
			else {
				System.out.println("neither");
			}
			
			// 다음 a, b 입력 받기
			a = scan.nextInt();
			b = scan.nextInt();
		}
	}
}
