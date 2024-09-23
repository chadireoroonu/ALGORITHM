import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char alphabet = s.charAt(i);
            if (!stack.isEmpty() && stack.peek() == alphabet) {
                stack.pop();
            } else {
                stack.push(alphabet);
            }
        }
        answer = stack.isEmpty() ? 1 : 0;
        
        return answer;
    }
}