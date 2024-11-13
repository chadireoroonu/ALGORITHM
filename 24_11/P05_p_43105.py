def solution(triangle):
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle[-1]))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])  + triangle[i][j]
    
    answer = max(dp[-1])
    return answer