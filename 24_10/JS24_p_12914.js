function solution(n) {
    var answer = 0;
    let dp = []
    
    for (let i = 0; i < n + 1; i++) {
        if (i < 2) {
            dp[i] = i + 1;
        } else {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        }
    }
    answer = dp[n-1];
    
    return answer;
}