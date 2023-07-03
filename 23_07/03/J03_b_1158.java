package month07;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class J03_b_1158 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int K = scan.nextInt();
		scan.close();
		
		// queue 생성 후 1~N 숫자 추가
		Queue<Integer> queue = new LinkedList<>();
		
		for (int i = 1; i < N+1; i++) {
			queue.add(i);
		}
		
		// K-1개의 숫자 맨 뒤로 이동 후 맨 앞 요소 출력 
		System.out.print("<");
		for (int j = 0; j < N-1; j++) {
			for (int k = 0; k < K-1; k++) {
				queue.add(queue.poll());
			}
			System.out.print(queue.poll()+", ");
		}
		System.out.print(queue.poll()+">");
	}
}
