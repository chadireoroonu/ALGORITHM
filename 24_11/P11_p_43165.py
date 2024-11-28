from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append((-1, 0))
    
    while queue:
        idx, now = queue.popleft()
        # numbers 마지막 도달 시
        if idx == len(numbers) - 1:
        	# target에 도착했다면 answer + 1
            if now == target:
                answer += 1
            continue
        
        # 현재 숫자를 뺀 값, 더한 값을 각각 큐에 추가
        queue.append((idx + 1, now - numbers[idx + 1]))
        queue.append((idx + 1, now + numbers[idx + 1]))
    
    return answer