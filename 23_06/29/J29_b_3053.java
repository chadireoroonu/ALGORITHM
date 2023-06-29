package day06261;

import java.util.*;

public class J29_b_3053 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		double r = scan.nextInt();
		scan.close();
		
		System.out.printf("%.6f", r*r*Math.PI); // PI 상수 활용
		System.out.println(); // 개행
		System.out.printf("%.6f", r*r*2.000000);
	}
}