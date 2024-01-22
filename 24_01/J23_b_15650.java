import java.util.Scanner;

public class Main {
	static boolean[] visited; // 중복 방문 방지
	static int[] array; // 수열 저장
	static int N;
	static int M;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		visited = new boolean[N];
		array = new int[M];
		
		DFS(0, 0);
	}
	
	static void DFS(int depth, int num) {
		// 수열이 채워졌으면 순서대로 출력
		if (depth == M) {
			for (int i : array) {
				System.out.print(i + " ");
			}
			System.out.println();
			return;
		}
		
		// 현재 번호 보다 큰 숫자들만 탐색
		for (int i = num; i < N; i++) {
			// 이전에 방문하지 않은 노드에 대하여
			if (!visited[i]) {
				visited[i] = true; // 방문 처리
				array[depth] = i + 1; // 수열 현재 깊이 자리에 i + 1 추가
				DFS(depth + 1, i); // 재귀 탐색
				visited[i] = false; // 자식 노드 탐색 후 방문 처리 초기화
			}
		}
	}
}
