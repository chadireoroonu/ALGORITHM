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
		
		// 입력 
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		result = new int[M];
		visited = new boolean[N];
		set = new LinkedHashSet<>();
		
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		
		// 정렬
		Arrays.sort(nums);
		
		// 함수 실행
		DFS(0, 0);
		
		// 결과 출력
		set.forEach(s -> System.out.println(s));
	}
	
	static void DFS(int depth, int now) {
		// 깊이 M 도달 시, 배열 Set에 추가
		if (depth == M) {
			String temp = "";
			for (int i : result) {
				temp += i + " ";
			}
			set.add(temp);
			return;
		}
		// 방문하지 않은 현재 숫자 이후 인덱스 방문
		for (int i = now; i < N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				result[depth] = nums[i];
				DFS(depth + 1, i);
				visited[i] = false;
			}
		}
	}
}
