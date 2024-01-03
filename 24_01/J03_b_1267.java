import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] array = new int[N];
		int M = 0;
		int Y = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			array[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < N; i++) {			
			Y += (array[i]/30 + 1) * 10;
			M += (array[i]/60 + 1) * 15;
			
		}

		if (Y <  M) {
			System.out.println("Y "+Y);
		}
		else if (M < Y) {
			System.out.println("M "+M);
		}
		else {
			System.out.println("Y M "+M);
		}
	}
}
