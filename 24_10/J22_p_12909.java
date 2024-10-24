import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            // 현재 괄호가 '('라면 스택에 추가
            if (now == '(') {
                stack.add(s.charAt(i));
            } else { // 현재 괄호가 ')'라면 스택 확인
            	// 스택이 비어있지 않다면 내부 요소 POP
                if (!stack.isEmpty()) {
                    stack.pop();
                } else { // 비어있다면 answer 재할당 및 중단
                    answer = false;
                    break;
                }
            }
        }
        // 모든 괄호 확인 후 남은 '(' 있다면 answer 재할당
        if (!stack.isEmpty()) {
            answer = false;
        }
        
        return answer;
    }
}