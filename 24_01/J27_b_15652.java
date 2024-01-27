import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] array;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		array = new int[M];
		
		DFS(0, 0);
		System.out.print(sb);
	}
	
	static void DFS(int depth, int num) {
		if (depth == M) {
			for (int i : array) {
				sb.append(i+ " ");
			}
			sb.append('\n');
			return;
		}
		for (int i = num; i < N; i++) {
			array[depth] = i + 1;
			DFS(depth + 1, i);
		}
	}
}