import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] check = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < n; i++) {
            if (!check[i]) {
                answer += 1;
                queue.add(i);
                while (!queue.isEmpty()) {
                    int x = queue.poll();
                    for (int nx = 0; nx < n; nx++) {
                        if (computers[x][nx] > 0 && !check[nx]) {
                            queue.add(nx);
                            check[nx] = true;
                        }
                    }
                }
            }
        }
        return answer;
    }
}