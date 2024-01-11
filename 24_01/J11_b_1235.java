import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String[] students = new String[n];
		HashSet<String> num = new HashSet<>();
		
		for (int i = 0; i < n; i++) {
			students[i] = br.readLine();
		}
		
		for (int i = 1; i <= students[0].length(); i++) {
			for (int j = 0; j < n; j++) {
				num.add(students[j].substring(students[0].length() - i));
			}
			
			if (num.size() == n) {				
				System.out.println(i);
				return;
			}
			num.clear();
		}
	}
}