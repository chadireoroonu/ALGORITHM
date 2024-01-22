import java.util.Scanner;

public class Main {
	static boolean[] visited; // 중복 방지
	static int[] array; // 수열 저장
	static int N;
	static int M;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		visited = new boolean[N];
		array = new int[M];
		
		DFS(0);
	}
	
	static void DFS(int depth) {
		// depth가 M과 같다면, 수열 내부 수 순서대로 출력
		if (depth == M) {
			for (int i : array) {
				System.out.print(i+ " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = 0; i < N; i++) {
			// 이전에 방문하지 않았던 노드에 대하여
			if (!visited[i]) {
				visited[i] = true; // 방문 체크
				array[depth] = i + 1; // 현재 깊이에 해당 수 추가
				DFS(depth + 1); // 깊이를 1 추가 후 DFS 탐색 
				visited[i] = false; // 방문 체크 되돌리기 
			}
		}
	}
}
