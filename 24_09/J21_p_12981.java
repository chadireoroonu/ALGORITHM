import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        
        // 나온 단어를 담을 Set 생성, 첫 단어 담기
        Set<String> check = new HashSet<>();
        check.add(words[0]);
        
        for (int i = 1; i < words.length; i++) {
            String word = words[i];
            // 이미 나온 단어 or 현 단어의 첫 단어가 전 단어의 마지막 단어와 다름
            if (check.contains(word) || word.charAt(0) != words[i-1].charAt(words[i-1].length() - 1)){
                answer = new int[]{i % n + 1, i / n + 1};
                return answer;
            }
            check.add(word);
        }
        return answer;
    }
}