import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
	static int N, M;
	static int[][] paper;
	static boolean[][] visited;
	static int num;
	static int[] di = {-1, 1, 0, 0};
	static int[] dj = {0, 0, -1, 1};
	
	static void BFS(int x, int y) {
		visited[x][y] = true;
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[]{x, y});
		
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int i = temp[0];
			int j = temp[1];
			
			for (int k = 0; k < 4; k++) {
				int ni = i + di[k];
				int nj = j + dj[k];
				
				if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
					if (paper[ni][nj] == 1 && !visited[ni][nj]) {
						num++;
						visited[ni][nj] = true;
						queue.add(new int[] {ni, nj});
					}
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer a = new StringTokenizer(br.readLine());
		
		boolean flag = true;
		List<Integer> result = new ArrayList<>();
		int maxi = 0;
		N = Integer.parseInt(a.nextToken());
		M = Integer.parseInt(a.nextToken());
		
		paper = new int[N][M];
		visited = new boolean[N][M];
		
		// 입력 받기
		for (int i = 0; i < N; i++) {
			StringTokenizer b = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				paper[i][j] = Integer.parseInt(b.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (paper[i][j] == 1 && !visited[i][j]) {
					flag = false;
					num = 1;
					BFS(i, j);
					result.add(num);
				}
			}
		}
		
		for (int i = 0; i < result.size(); i++) {
			if (result.get(i) > maxi) {
				maxi = result.get(i);
			}
		}
		
		if (flag) {
			System.out.println(0);
			System.out.println(0);
		}
		else {
			System.out.println(result.size());
			System.out.println(maxi);
		}
	}
}
