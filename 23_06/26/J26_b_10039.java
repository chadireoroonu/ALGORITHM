package day06261;

import java.util.*;

public class J26_b_10039 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int total = 0; // 총 점수 합산
		
		// 다섯 명 점 수 입력
		for(int i=0; i<5; i++) {
			int temp = scan.nextInt();
			
			// 40점 이하 점수 보정
			if (temp < 40) {
				temp = 40;
			}
			total += temp;
		}
		// 평균 출력
		System.out.println(total/5);
	}
}