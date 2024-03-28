import sys
from collections import deque
sys.stdin = open("../temp/input.txt")


def BFS(n):
    queue = deque([n])
    visited = [-1] * 10001  # 방문 확인 및 거리 저장
    visited[n] = 0  # 현재 노드까지의 거리 설정
    while queue:
        x = queue.popleft()
        # x와 연결된 도시 방문
        for nx, add in world[x]:
            # 방문한 적이 없는 도시라면, 거리 저장
            if visited[nx] < 0:
                visited[nx] = visited[x] + add
                queue.append(nx)
    return visited


world = [[] for _ in range(10001)]  # 최대 수 10000 고려
while True:  # 입력이 있는 만큼 처리
    try:
        s, e, d = map(int, sys.stdin.readline().split())
        world[s].append([e, d])
        world[e].append([s, d])
    except:
        break

temp = BFS(1)  # 아무 지점에서나 가장 거리가 먼 노드 탐색
idx = temp.index(max(temp))  # 가장 거리가 먼 노드 인덱스 저장

temp = BFS(idx)  # 인덱스 노드에서 가장 거리가 먼 노드 탐색
print(max(temp))  # 최장거리 출력
