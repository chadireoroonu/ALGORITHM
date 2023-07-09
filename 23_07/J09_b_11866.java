package month07;

import java.util.LinkedList;
import java.util.Scanner;

public class J09_b_11866 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int K = scan.nextInt();
		
		LinkedList<Integer> queue = new LinkedList<>();
		
		// queue 요소 추가
		for (int i = 1; i <= N; i++) {
			queue.add(i);
		}
		
		System.out.print("<");
		// K 번째 수 출력 N-1회 반복
		for (int j = 0; j < N-1; j++) {
			for (int k = 0; k < K-1; k++) {
				queue.addLast(queue.pollFirst());
			}
			System.out.print(queue.poll()+", ");
		}
		// 마지막 요소 출력
		System.out.println(queue.poll()+">");
	}
}
