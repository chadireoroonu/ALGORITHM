import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] nums = new int[N];
		int[] sums = new int[N+1]; // 누적 합
		
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
			if (i > 0) {
				sums[i] = nums[i-1] + sums[i-1];
			}
		}
		sums[N] = nums[N-1] + sums[N-1]; // 마지막 누적합 칸 채우기
		
		for (int j = 0; j < M; j++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(sums[end]-sums[start-1]);
		}
	}
}