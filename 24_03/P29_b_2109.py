import sys, heapq
sys.stdin = open("../temp/input.txt")

n = int(sys.stdin.readline())
order = []  # 마감일 정렬 들어온 제안
choice = []  # 강연료 정렬 선택한 제안

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    heapq.heappush(order, [d, p])  # 마감일 기준 정렬로 힙큐 추가

while order:  # 모든 제안에 대해 마감일 오름차순 진행
    d, p = heapq.heappop(order)
    # 마감일 안에 강연이 가득차 있지 않다면 해당 제안 선택
    if d > len(choice):
        heapq.heappush(choice, p)
    else:
        # 마감일 안에 강연이 가득차있다면 강연료 비교 후 선택 결정
        if p > choice[0]:
            heapq.heappop(choice)
            heapq.heappush(choice, p)

# 선택한 제안의 강연료 합 출력
print(sum(choice))
