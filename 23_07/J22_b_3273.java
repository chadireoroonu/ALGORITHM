import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
        int[] nums = new int[n];
        int count = 0;
        
        for (int i = 0; i < n; i++) {
        	nums[i] = scan.nextInt();
        }
        int x = scan.nextInt();
        int front = n-1;
        int rear = 0;
        
        // 배열 정렬
        Arrays.sort(nums);
        
        while (rear < front) {
        	// 두 수의 합이 x라면 count += 1, rear += 1
        	if (nums[front] + nums[rear] == x) {
        		count += 1;
        		rear += 1;
        	}
        	// 두 수의 합이 x보다 크다면 front -= 1
        	else if (nums[front] + nums[rear] > x) {
        		front -=1;
        	}
        	// 두 수의 합이 x보다 작다면 rear += 1
        	else {
        		rear += 1;
        	}
        }
        System.out.println(count);        	
	}
}
