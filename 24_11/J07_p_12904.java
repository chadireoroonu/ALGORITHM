class Solution
{
    public int solution(String s)
    {
        int answer = 0;
		// i : 왼쪽 ~ 마지막, j : 마지막 ~ i
        for (int i = 0; i < s.length(); i++) {
            for (int j = s.length() - 1; j > i - 1; j--) {
            	// 현재 검사의 최대길이 유망성 확인
                if (j - i + 1 < answer) {
                    continue;
                }
                // 팰린드롬 여부 및 포인터
                boolean palindrome = true;
                int left = i;
                int right = j;
                while (left < right) {
                	// 포인터가 가리키는 글자가 같다면 다음 글자 확인
                    if (s.charAt(left) == s.charAt(right)) {
                        left++;
                        right--;
                    }
                    // 포인터가 가리키는 글자가 다르면 팰린드롬 변경 및 종료
                    else {
                        palindrome = false;
                        break;
                    }
                }
                // 현재가 팰린드롬이고 저장된 최댓값보다 크다면 answer 재할당
                if (palindrome && answer < j - i + 1) {
                    answer = j - i + 1;
                }
            }
        }
        return answer;
    }
}