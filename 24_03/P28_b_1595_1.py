import sys, heapq
sys.stdin = open("../temp/input.txt")


def sol(n):
    queue = []
    visited = [1] * 10001  # 방문 확인 및 거리 저장
    visited[n] = 0  # 현재 노드까지의 거리 설정
    heapq.heappush(queue, [0, n])
    while queue:
        cost, x = heapq.heappop(queue)
        if cost > visited[x]:
            continue
        for add, nx in world[x]:
            if visited[nx] > 0:  # 방문하지 않은 도시 방문 처리
                visited[nx] = cost + add
                heapq.heappush(queue, [cost + add, nx])
            if cost + add > visited[nx]:  # 더 빠른 거리 발견 시 거리 재설정
                visited[nx] = cost + add
                heapq.heappush(queue, [cost + add, nx])
    return visited


world = [[] for _ in range(10001)]  # 최대 수 10000 고려
while True:  # 입력이 있는 만큼 처리
    try:
        s, e, d = list(map(int, sys.stdin.readline().split()))
        world[s].append([-d, e])  # 최대힙으로 사용하기 위해 음수로 저장
        world[e].append([-d, s])
    except:
        break

temp = sol(1)  # 아무 도시에서나 가장 거리가 먼 도시 탐색
idx = temp.index(min(temp[1:]))  # 가장 거리가 먼 도시 정보

temp = sol(idx)  # 찾은 도시에서 가장 거리가 먼 도시
print(-min(temp[1:]))  # 가장 먼 두 도시의 거리 출력
