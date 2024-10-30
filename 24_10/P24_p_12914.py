def solution(n):
    answer = 0
    dp = [0] * (n+1)
    for i in range(n):
        if i < 2:
            dp[i] = i + 1
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    answer = dp[n-1]
    return answer