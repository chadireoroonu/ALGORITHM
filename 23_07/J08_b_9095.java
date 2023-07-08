package month07;

import java.util.Scanner;

public class J08_b_9095 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();
		
		int[] array = new int[11];
		
		// 초기 정보
		array[1] = 1;
		array[2] = 2;
		array[3] = 4;
		
		// 1~11 방법의 수 기록
		for (int i = 4; i < 11; i++) {
			array[i] = array[i-1] + array[i-2] + array[i-3];
		}
		
		for (int j = 0; j < T; j++) {
			System.out.println(array[scan.nextInt()]);
		}
	}
}
