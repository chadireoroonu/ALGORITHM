import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        int idx, now;
        
        // 이전까지 인덱스, 총합 저장할 큐 및 초기세팅
        Queue<Integer> queue = new LinkedList<>();
        queue.add(-1);
        queue.add(0);
        
        // 큐가 있는 동안 idx, now 추출
        while (!queue.isEmpty()) {
            idx = queue.poll();
            now = queue.poll();
            
            // 현재 idx가 마지막을 가리키면 continue
            if (idx == numbers.length - 1) {
            	// 현재 총합이 타겟과 같으면 answer++
                if (now == target) {
                    answer++;
                }
                continue;
            }
            // 다음 인덱스, 총계 - 현재값, 총계 + 현재값 큐 추가
            queue.add(idx + 1);
            queue.add(now - numbers[idx + 1]);
            queue.add(idx + 1);
            queue.add(now + numbers[idx + 1]);
        }
        return answer;
    }
}