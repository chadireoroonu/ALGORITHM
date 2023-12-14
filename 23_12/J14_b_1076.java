import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] colors = {"black", "brown", "red", "orange",
				"yellow", "green", "blue", "violet", "grey", "white"};
		
		long result = 0;
		
		String X = br.readLine();
		String Y = br.readLine();
		String Z = br.readLine();
		
		result += Arrays.asList(colors).indexOf(X) * 10;
		result += Arrays.asList(colors).indexOf(Y);
		result *= Math.pow(10, Arrays.asList(colors).indexOf(Z));
		
		System.out.println(result);
	}
}