import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int group = 1;
		
		while (true) {
			int N = Integer.parseInt(br.readLine());
			boolean flag = true;
			
			if (N == 0) break;
			
			// 정보 입력 받기
			String[][] array = new String[N][N];
			
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					array[i][j] = st.nextToken();
				}
			}
			
			System.out.println("Group " + group);
			
			// 나쁜말 검사 및 출력
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (array[i][j].equals("N")) {
						if (i < j) {
							System.out.println(array[N - j + i][0] + " was nasty about " + array[i][0]);
						}
						else {
							System.out.println(array[i - j][0] + " was nasty about " + array[i][0]);
						}
						flag = false;
					}
				}
			}
			
			if (flag) System.out.println("Nobody was nasty");
			System.out.println();
			group += 1;
		}
	}
}
