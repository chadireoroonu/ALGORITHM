import heapq

def pop(queue, arr): # 이중우선순위 큐 pop 연산
    while queue:
        num, index = heapq.heappop(queue)
        if arr[index]: # 유효성 검사
            return num, index
    return 0, 0 # 이중우선순위 큐가 비어있을 경우

def solution(operations):
    answer = []
    minq, maxq = [], [] # 최소힙, 최대힙
    check = [False] * (len(operations) + 1) # 유효성
    
    for i in range(1, len(operations) + 1):
        alphabet, num = map(str, operations[i - 1].split())
        if alphabet == "I": # 숫자 추가
            heapq.heappush(minq, (int(num), i))
            heapq.heappush(maxq, (-int(num), i))
            check[i] = True
        else:
            if num == "1": # 최대힙 삭제
                check[pop(maxq, check)[1]] = False
            else: # 최소힙 삭제
                check[pop(minq, check)[1]] = False
    
    answer.append(-pop(maxq, check)[0]) # 최댓값
    answer.append(pop(minq, check)[0]) # 최솟값
    
    return answer