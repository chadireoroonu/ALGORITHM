import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken()) - 1;
		int M = Integer.parseInt(st.nextToken()) - 1;

		int x1 = N / 4;
		int y1 = N % 4;

		int x2 = M / 4;
		int y2 = M % 4;

		System.out.println(Math.abs(x1 - x2) + Math.abs(y1 - y2));
	}
}