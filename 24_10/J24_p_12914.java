class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] dp = new int[n+1]; // 1 런타임 에러 방지
        
        for (int i = 0; i < n; i++) {
            // 0, 1 예외처리
            if (i < 2) {
                dp[i] = (i + 1) % 1234567;
            } else {
                dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
            }
        }
        
        answer = dp[n-1];
        return answer;
    }
}