import sys, heapq
sys.stdin = open("../temp/input.txt")

N, K = map(int, sys.stdin.readline().split())
devices = list(map(int, sys.stdin.readline().split()))
order = [[] for _ in range(K + 1)]  # 사용 순서
count = 0  # 플러그 제거 횟수

for i in range(K):
    heapq.heappush(order[devices[i]], i)

docking = set()  # 현재 연결된 디바이스
plugs = []  # 최대힙
for device in devices:
    heapq.heappop(order[device])  # 사용 표시
    # 디바이스 플러그가 연결되어 있지 않고, 연결된 플러그가 가득찬 경우
    if device not in docking and len(docking) == N:
        # 다음 사용 순서가 가장 늦은 플러그 제거 후 count + 1
        _, target = heapq.heappop(plugs)
        docking.remove(target)
        count += 1
    # 현재 사용할 디바이스의 플러그 연결
    docking.add(device)
    if order[device]:  # 현재 사용할 디바이스의 재사용 계획이 있을 경우
        heapq.heappush(plugs, [-order[device][0], device])
    else:  # 현재 사용할 디바이스의 재사용 계획이 없을 경우
        heapq.heappush(plugs, [-(K + 1), device])

print(count)
