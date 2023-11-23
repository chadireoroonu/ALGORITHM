import java.util.Scanner;

public class Main {
	
	static int[] nums;
	static int N;
	static int S;
	static int result = 0;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		N = scan.nextInt();
		S = scan.nextInt();
		nums = new int[N];
		
		// 배열 입력
		for (int i = 0; i < N; i++) {
			nums[i] = scan.nextInt();
		}
		
		dfs(0, 0);
		if (S != 0) {
			System.out.println(result);
		} else {
			System.out.println(result-1);
		}
	}
		
	public static void dfs(int D, int M) {
		if (D == N) {
			if (M == S) {
				result += 1;
			} 
			return;
		}	
		dfs(D+1, M+nums[D]);
		dfs(D+1, M);
	}	
}
