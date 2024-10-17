import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int N = maps.length, M = maps[0].length;
        int visited[][] = new int[N][M];
        
        // queue 생성 및 초기 위치 추가
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        queue.add(0);
        
        // BFS
        while (!queue.isEmpty()) {
            // 현재위치 및 4방향 지표
            int i = queue.poll(), j = queue.poll();       
            int[] di = {-1, 1, 0, 0}, dj = {0, 0, -1, 1};
            
            // 4방향 탐색
            for (int k = 0; k < 4; k++) {
                int ni = i + di[k], nj = j + dj[k];
                
                // 맵 범위 내에 있으며 방문한 적이 없고 길이 있다면
                // 방문 기록 및 큐에 추가
                if (0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if (visited[ni][nj] == 0 && maps[ni][nj] == 1) {
                        visited[ni][nj] = visited[i][j] + 1;
                        queue.add(ni);
                        queue.add(nj);
                    }
                }
            }
        }
        // 상대방 진영까지의 칸 수 혹은 방문불가 여부 저장
        answer = visited[N-1][M-1] > 0 ? visited[N-1][M-1] + 1 : -1;
        return answer;
    }
}