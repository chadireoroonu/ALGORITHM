package month07;

import java.util.LinkedList;
import java.util.Scanner;

public class J07_b_1021 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int M = scan.nextInt();
		int shift = 0;
		
		LinkedList<Integer> queue = new LinkedList<>();
		
		for (int i = 1; i <= N; i++) {
			queue.add(i);
		}
		
		for (int j = 0; j < M; j++) {
			int target = queue.indexOf(scan.nextInt());
			if (target < queue.size() - target) {
				for (int k = 0; k < target; k++) {
					queue.addLast(queue.poll());
					shift += 1;
				}
			}
			else {
				for (int k= 0; k < queue.size() - target; k++) {
					queue.addFirst(queue.pollLast());
					shift += 1;
				}
			}
			queue.remove();
		}
		System.out.println(shift);
	}
}
