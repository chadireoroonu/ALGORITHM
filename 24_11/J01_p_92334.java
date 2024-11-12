import java.util.HashMap;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int N = id_list.length;
        int[] answer = new int[N];
        int[] counts = new int[N];
        HashMap<String, Integer> people = new HashMap<String, Integer>();
        boolean[][] complain = new boolean[N][N];
        
        // 이름 : 숫자 짝지어주기
        for (int i = 0; i < N; i++) {
            people.put(id_list[i], i);
        }
        
        // 신고 정보 입력 처리
        for (int i = 0; i < report.length; i++) {
            String[] info = report[i].split(" ");
            // 타인에 대한 신고는 한 명당 한 번만 신고 가능
            if (complain[people.get(info[0])][people.get(info[1])] == false) {
                complain[people.get(info[0])][people.get(info[1])] = true;
                counts[people.get(info[1])]++;
            }
        }
        
        // 내가 신고한 사람이 중지당한 사람인지 확인
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (complain[i][j] == true && counts[j] >= k) {
                    answer[i]++;
                }
            }
        }
        
        return answer;
    }
}