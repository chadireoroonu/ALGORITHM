import java.util.Scanner;

public class Main {
	
	static int N, M;
	static int[] array;
	// 시간초과 방지를 위한 출력 방식
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		array = new int[M];
		
		DFS(0);
		System.out.print(sb);
	}
	
	// 중복 여부를 고려하지 않고, 배열에 수 추가
	static void DFS(int depth) {
		if (depth == M) {
			for (int i : array) {
				sb.append(i + " ");
			}
			sb.append('\n');
			return;
		}
		
		for (int i = 0; i < N; i++) {
			array[depth] = i + 1;
			DFS(depth + 1);
		}
	}
}
