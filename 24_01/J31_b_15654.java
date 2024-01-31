import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] result;
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		nums = new int[N]; // 주어진 숫자 저장
		result = new int[M]; // 출력할 배열
		visited = new boolean[N];
		
		StringTokenizer num = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(num.nextToken());
		}

		// 주어진 숫자들 정렬
		Arrays.sort(nums);
		
		DFS(0);
		System.out.println(sb);
	}
	
	static void DFS(int depth) {
        // 깊이 조건 만족 시 result 요소들 sb에 추가
		if (depth == M) {
			for (int i : result) {
				sb.append(i + " ");
			}
			sb.append('\n');
			return;
		}
        // 방문하지 않은 숫자에 대해 방문 및 재귀호출
		for (int i = 0; i < N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				result[depth] = nums[i];
				DFS(depth+1);
				visited[i] = false;
			}
		}
	}
}
