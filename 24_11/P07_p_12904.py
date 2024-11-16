def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(len(s) - 1, i - 1, -1):
            # 최댓값 유망성 검사
            if j - i + 1 < answer:
                continue
            palindrome = True
            left, right = i, j # 포인터
            while left < right:
            	# 포인터가 가리키는 글자가 같으면, 다음 글자 검사
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                # 포인터가 가리키는 글자가 다르면 종료
                else:
                    palindrome = False
                    break
            # 팰린드롬이라면, 길이 비교 후 최댓값 저장
            answer = max(answer, j - i + 1) if palindrome else answer
    return answer