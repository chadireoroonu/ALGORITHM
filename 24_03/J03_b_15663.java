import java.util.Scanner;
import java.util.Arrays;
import java.util.Set;
import java.util.LinkedHashSet;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] result;
	static boolean visited[];
	static Set<String> set;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		result = new int[M];
		visited = new boolean[N];
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
			if (!visited[i]) {
				result[depth] = nums[i];
				visited[i] = true;
				DFS(depth + 1);
				visited[i] = false;
			}
		}
	}
}
