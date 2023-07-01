import java.util.Scanner;

public class J01_b_10824 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String a = scan.next();
		String b = scan.next();
		String c = scan.next();
		String d = scan.next();
		scan.close();
		
		Long ab = Long.parseLong(a+b);
		Long cd = Long.parseLong(c+d);
		
		System.out.println(ab+cd);
	}
}
