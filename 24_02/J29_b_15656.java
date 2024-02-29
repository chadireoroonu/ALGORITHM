import java.util.Scanner;
import java.util.Arrays;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] result;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 초기 설정
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		result = new int[M];
		
		// 입력받기
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		
		// 배열 정렬
		Arrays.sort(nums);
		
		DFS(0);
		System.out.println(sb);
	};
	
	static void DFS(int depth) {
		// 깊이가 M인 경우, 현재 result 요소들을 sb에 추가
		if (depth == M) {
			for (int i : result) {
				sb.append(i+" ");
			}
			sb.append('\n');
			return;
		}
		// 그렇지 않으면 재귀호출로 다음 숫자 추가
		for (int i = 0; i < N; i++) {
			result[depth] = nums[i];
			DFS(depth+1);
		}
	}
}
