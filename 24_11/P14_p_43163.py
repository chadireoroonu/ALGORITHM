from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words) # 방문여부 확인
    queue = deque()
    queue.append((begin, 0)) # 최초 단어, 변환횟수
    
    while queue:
    	# 현재단어, 현재까지 변환횟수
        before, count = queue.popleft()
        for i in range(len(words)):
            after = words[i]
            miss = 0 # 다른 알파벳 수
            for j in range(len(after)):
                if before[j] != after[j]:
                    miss += 1
            # 한 단어만 다르고, 방문하지 않은 단어일 경우
            if miss == 1 and not visited[i]:
            	# 현재 단어가 목표단어일 경우
                if after == target:
                    return count + 1
                queue.append((after, count + 1))
                visited[i] = True
    
    return answer