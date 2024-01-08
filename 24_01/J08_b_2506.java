import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int add = 1;
		int point = 0;
		
		for (int i = 0; i < N; i++) {
			if (sc.nextInt() == 1) {
				point += add;
				add ++;
			}
			else add = 1;
		}
		
		System.out.println(point);
	}
}
