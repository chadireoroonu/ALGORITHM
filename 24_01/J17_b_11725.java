import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	static int N;
	static int[] parent;
	static ArrayList<Integer> children[];
	static boolean[] visited;
	
	static void find(int n) {
		
		for (int i: children[n]) {
			if (!visited[i]) {
				parent[i] = n;
				visited[i] = true;
				find(i);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		parent = new int[N + 1]; 
		children = new ArrayList[N + 1];
		visited = new boolean[N + 1];
		
		for (int i = 0; i < N + 1; i++) {
			children[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < N - 1; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			children[s].add(e);
			children[e].add(s);
			
		}
		
		visited[1] = true;
		find(1);
		
		for (int i = 2; i < N + 1; i++) {
			System.out.println(parent[i]);
		}
	}
}
