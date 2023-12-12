import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			int result = 1;
			String temp = br.readLine();
			int nums = temp.length();
			if (nums == 1 && temp.charAt(0) == '0') {
				break;
			}

			for (int i = 0; i < nums; i++) {
				if (temp.charAt(i) == '1') {
					result += 3;
				}
				else if (temp.charAt(i) == '0') {
					result += 5;
				}
				else {
					result += 4;
				}
			}
			System.out.println(result);
		}
	}
}
