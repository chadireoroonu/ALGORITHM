import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[][] room = new String[N][N];
		int horizontal = 0;
		int vertical = 0;
		boolean HFlag;
		boolean VFlag;
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String temp = st.nextToken();
			for (int j = 0; j < N; j++) {
				room[i][j] = Character.toString(temp.charAt(j));
			}
		}
		
		for (int i = 0; i < N; i++) {
			HFlag = true;
			VFlag = true;
			for (int j = 0; j < N-1; j++) {
				if (room[i][j].equals("X")) HFlag = true;
				if (room[i][j].equals(".") && room[i][j+1].equals(".") && HFlag) {
					horizontal++;
					HFlag = false;
				}
				if (room[j][i].equals("X")) VFlag = true;
				if (room[j][i].equals(".") && room[j+1][i].equals(".") && VFlag) {
					vertical++;
					VFlag = false;
				}
				
			}
		}
		
		System.out.println(horizontal+" "+vertical);
	}
}
