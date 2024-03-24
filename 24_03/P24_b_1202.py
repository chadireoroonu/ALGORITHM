import sys, heapq
sys.stdin = open("../temp/input.txt")

N, K = list(map(int, sys.stdin.readline().split()))
jewels = []  # 보석 무게, 가치 정보
bags = []  # 가방 무게 정보
temp = []  # 가방에 들어갈 수 있는 보석 정보
value = 0  # 총 가치

for _ in range(N):  # 보석 정보 입력 처리
    M, V = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(jewels, [M, -V])

for _ in range(K):  # 가방 정보 입력 처리
    C = int(sys.stdin.readline())
    bags.append(C)

bags.sort()  # 가방 정렬

for bag in bags:
    # 보석 무게가 현재 가방 무게보다 작거나 같은 경우
    while jewels and bag >= jewels[0][0]:
        # 보석 정보 temp 저장
        M, V = heapq.heappop(jewels)
        heapq.heappush(temp, V)
    # 담을 수 있는 보석이 있다면, 가장 가치가 높은 것 담기
    if temp:
        value -= heapq.heappop(temp)

print(value)
