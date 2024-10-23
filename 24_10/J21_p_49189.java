import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int[] distance = new int[n];
        boolean [][] loads = new boolean[n][n];
        int maxi = 0;
        
        // 연결 정보 저장
        for (int i = 0; i < edge.length; i++) {
            loads[edge[i][0] - 1][edge[i][1] - 1] = true;
            loads[edge[i][1] - 1][edge[i][0] - 1] = true;
        }
        
        // 거리 조사 준비
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        distance[0] = 1;
        
        while (!queue.isEmpty()) {
            int x = queue.poll();
            
            // X와 연결되어 있는 미방문 노드를 찾아 거리 기록
            for (int k = 0; k < n; k++) {
                if (loads[x][k] && distance[k] == 0) {
                    distance[k] = distance[x] + 1;
                    
                    // 최대 거리 갱신
                    if (maxi < distance[x] + 1) {
                        maxi = distance[x] + 1;
                    }
                    queue.add(k);
                }
            }
        }
        
        // 최대 거리 노드 수 세기
        for (int i = 0; i < n; i++) {
            if (distance[i] == maxi) {
                answer++;
            }
        }
        return answer;
    }
}