import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Collections;

public class J13_b_1764 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N, M;
		int num = 0;
		HashSet<String> people = new HashSet<>(); 
		ArrayList<String> result = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			people.add(br.readLine());
		}
		
		for (int i = 0; i < M; i++) {
			String person = br.readLine();
			if (people.contains(person)) {
				num ++;
				result.add(person);
			}
		}
		
		Collections.sort(result);
		System.out.println(num);
		
		for (int i = 0; i < num; i++) {
			System.out.println(result.get(i));
		}
	}
}
