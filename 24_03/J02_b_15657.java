import java.util.Scanner;
import java.util.Arrays;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] result;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		result = new int[M];
		
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		
		Arrays.sort(nums);
		
		DFS(0, 0);
		System.out.println(sb);
	}
	
	static void DFS(int depth, int now) {
		if (depth == M) {
			for (int i : result) {
				sb.append(i+" ");
			}
			sb.append('\n');
			return;
		}
		for (int i = now; i < N; i ++) {
			result[depth] = nums[i];
			DFS(depth + 1, i);
		}
	}
}
