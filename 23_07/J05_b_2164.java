package month07;

import java.util.LinkedList;
import java.util.Scanner;

public class J05_b_2164 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		scan.close();
		
		// queue 요소 추가
		LinkedList<Integer> queue = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			queue.addLast(i);
		}
		
		// queue 길이가 1이 될 때 까지 문제 조건 반복
		while (queue.size() > 1) {
			queue.pollFirst();
			queue.addLast(queue.pollFirst());
		}
		System.out.println(queue.pollFirst());
	}
}
