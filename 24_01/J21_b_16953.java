import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
	static long A;
	static long B;
	static boolean flag = false;
	
	static void DFS(long s, int count) {
		if (s < B) {
			long next1 = s * 2;
			String temp = Long.toString(s) + "1";
			long next2 = Long.parseLong(temp);
			
			if (next1 == B || next2 == B) {
				System.out.println(count + 1);
				flag = true;
				return;
			}
			else {
				DFS(next1, count + 1);
				DFS(next2, count + 1);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		A = sc.nextLong();
		B = sc.nextLong();
		
		DFS(A, 1);
		
		if (!flag) {
			System.out.println(-1);			
		}
	}
}