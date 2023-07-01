# 각 섬 구분을 위해 섬의 고유 숫자 설정
# 바다와 인접한 모든 육지에서 BFS 탐색 진행
# 각 진행 지점에서 타 섬으로의 최소 거리 찾는 함수 실행

import sys
from collections import deque
sys.stdin = open('input.txt')

# 섬 고유 숫자 설정
def islandnum(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and world[ni][nj] == 1:
                world[ni][nj] = island
                queue.append((ni, nj))
    return

def bridge(i, j, num):
    global mini
    temp = N * N
    queue = deque()
    queue.append((i, j))
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                # 바다
                if not world[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
                # 다른 섬
                if world[ni][nj] and world[ni][nj] != num:
                    return visited[ni][nj]
    return print(0)

N = int(sys.stdin.readline().strip())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

island = 1
mini = N * N

for x in range(N):
    for y in range(N):
        if world[x][y] == 1:
            island += 1
            world[x][y] = island
            islandnum(x, y)

for x in range(N):
    for y in range(N):
        mini = min(mini, bridge(x))

print(mini)

# 한 섬의 끝에서 다른 섬까지의 거리 계산