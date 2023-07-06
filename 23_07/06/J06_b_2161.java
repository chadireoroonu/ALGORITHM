package month07;

import java.util.LinkedList;
import java.util.Scanner;

public class J06_b_2161 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		scan.close();
		
		LinkedList<Integer> queue = new LinkedList<>();
		
		// 큐에 카드 넣기
		for (int i = 1; i <= N; i++) {
			queue.add(i);
		}
		
		// 문제 조건 따라 요소 출력
		while (queue.size() > 1) {
			System.out.print(queue.pollFirst() + " ");
			queue.add(queue.pollFirst());
		}
		System.out.println(queue.pollFirst());
	}
}
