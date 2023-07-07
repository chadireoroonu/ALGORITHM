package day06261;

import java.util.*;

public class J30_b_2501 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int A = scan.nextInt();
		int K = scan.nextInt();
		scan.close();
		int t = 0; // K번째 까지 셀 변수
		
		for (int i = 1; i <= A; i++) {
			if (A % i == 0) { // i가 A의 약수라면 t 증가
				t += 1;
				if (K == t) { // i가 K번째 약수라면 출력 후 중단
					System.out.println(i);
					break;
				}
			}
			if (i == A && t < K) { // K번째 약수가 없다면 0 출력
				System.out.println(0);
			}
		}
	}
}
