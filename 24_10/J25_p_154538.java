import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] counts = new int[y+1];
        int[] di = {n, 2, 3};
        
        counts[x] = 1;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        
        while (!queue.isEmpty()) {
            int i = queue.poll();
            for (int k = 0; k < 3; k++) {
                int ni = k == 0 ? i + di[k] : i * di[k];
                if (ni <= y) {
                    if (counts[ni] < 1 || counts[ni] > counts[i] + 1) {
                        counts[ni] = counts[i] + 1;
                        queue.add(ni);
                    }
                }   
            }
        }
        answer = counts[y] > 0 ? counts[y]-1 : -1;
        
        return answer;
    }
}