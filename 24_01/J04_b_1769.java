import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String N = br.readLine();
		int count = 0;
		
		while(true) {
			if (N.length() == 1) {
				break;
			}
			int temp = 0;
			
			for (int i = 0; i < N.length(); i++) {
				temp += Integer.parseInt(String.valueOf(N.charAt(i)));
			}
			count += 1;
			N = String.valueOf(temp);
		}
		
		System.out.println(count);
		if (Integer.parseInt(String.valueOf(N)) % 3 == 0) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}
}
