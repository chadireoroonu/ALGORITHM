import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {        
        
        // 각 기능 완료일
        double[] days = new double[speeds.length];
        for (int i = 0; i < speeds.length; i++) {
            double day = Math.ceil((100.0-progresses[i])/speeds[i]);
            days[i] = day;
        }
        
        // 배포일별 배포 기능 수
        ArrayList<Integer> list = new ArrayList<>();
        int pointer = 0;
        for (int i = 1; i < days.length; i++) {
            if (days[i] > days[pointer]) {
                list.add(i - pointer);
                pointer = i;
            }
        }
        list.add(days.length - pointer);
        
        // 형변환
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}