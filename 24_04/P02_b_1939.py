import sys, heapq
sys.stdin = open("../temp/input.txt")

N, M = map(int, sys.stdin.readline().split())
loads = [[] for _ in range(N + 1)]  # 다리 연결 및 중량제한

for _ in range(M):  # 최대힙으로 사용하기 위해 -C 형태로 저장
    A, B, C = map(int, sys.stdin.readline().split())
    loads[A].append([-C, B])
    loads[B].append([-C, A])

S, E = map(int, sys.stdin.readline().split())
maxi = [0] * (N + 1)  # 출발지에서 각 섬까지의 최대 중량

queue = []
heapq.heappush(queue, [-10 ** 9, S])  # 최대치로 초기 설정
while queue:
    cost, x = heapq.heappop(queue)
    # 목적지에 도착했다면 중단
    if x == E:
        break
    # 현재 무게보다 더 큰 중량제한이 저장되어 있다면 무시
    if maxi[x] < cost:
        continue
    # 연결된 섬까지 중량제한, 섬 번호 저장
    for temp, nx in loads[x]:
        # cost, temp 중 작은 중량제한 선택
        select = max(cost, temp)
        # 저장된 무게보다 큰 중량제한일 경우 maxi 재할당
        if maxi[nx] > select:
            maxi[nx] = select
            heapq.heappush(queue, [select, nx])

print(-maxi[E])
