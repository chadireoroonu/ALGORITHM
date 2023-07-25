package month07;

import java.util.Scanner;

public class J25_b_1138 {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		int[] array = new int[N];
		
		for (int i = 0; i < N; i++) {
			int order = scan.nextInt();
			int temp = 0;
			
			for (int j = 0; j < N; j++) {
				// 왼쪽에 올 큰 수 만큼 건너 뛴 후, 빈 자리에 숫자 추가
				if (order == temp && array[j] == 0) {
					array[j] = i+1;
					break;	
				}
				// 만약 아직 채워지지 않은 자리는 더 큰 수 자리
				if (array[j] == 0) {
					temp += 1;
				}
			}
		}
		for (int k = 0; k < N; k++) {
			System.out.print(array[k]+" ");
		}
	}
}
