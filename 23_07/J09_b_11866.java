package month07;

import java.util.LinkedList;
import java.util.Scanner;

public class J09_b_11866 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int K = scan.nextInt();
		
		LinkedList<Integer> queue = new LinkedList<>();
		
		for (int i = 1; i <= N; i++) {
			queue.add(i);
		}
		
		System.out.print("<");
		for (int j = 0; j < N-1; j++) {
			for (int k = 0; k < K-1; k++) {
				queue.addLast(queue.pollFirst());
			}
			System.out.print(queue.poll()+", ");
		}
			
		System.out.println(queue.poll()+">");
	}
}
