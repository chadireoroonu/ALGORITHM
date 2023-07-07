package day06261;

import java.util.*;

public class J27_b_11721 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String word = scan.next();
		scan.close();
		
		for (int i = 0; i < word.length(); i++) {
			System.out.print(word.charAt(i));
			
			// 출력 글자가 10개라면 개행
			if (i % 10 == 9) {
				System.out.println();				
			}
		}
	}
}