import java.util.Scanner;
import java.util.Arrays;
import java.util.Set;
import java.util.LinkedHashSet;


public class J09_b_15665 {
	static int N, M;
	static int[] nums, result;
	static Set<String> set;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		result = new int[M];
		set = new LinkedHashSet<>();
		
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		
		Arrays.sort(nums);
		DFS(0);
		
		set.forEach(s -> System.out.println(s));
	}
	static void DFS(int depth) {
		if (depth == M) {
			String temp = "";
			for (int i : result) {
				temp += i + " ";
			}
			set.add(temp);
			return;
		}
		for (int i = 0; i < N; i++) {
			result[depth] = nums[i];
			DFS(depth + 1);
		}
	}
}
