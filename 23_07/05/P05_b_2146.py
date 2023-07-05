import sys
from collections import deque
sys.stdin = open('input.txt')

# 섬 고유번호 설정 함수
def islandnum(a, b, num):
    queue = deque()
    queue.append((a, b))
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and world[ni][nj] == 1:
                world[ni][nj] = num
                queue.append((ni, nj))
    return

# 다리 구축 함수
def bridge(a, b, num):
    queue = deque()
    queue.append((a, b))
    visited = [[0]*N for _ in range(N)]
    visited[a][b] = 1
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
                    return visited[i][j] - 1
    return N ** N

N = int(sys.stdin.readline().strip())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

island = 2
mini = N ** N

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 섬 고유번호 설정
for x in range(N):
    for y in range(N):
        if world[x][y] == 1:
            world[x][y] = island
            islandnum(x, y, island)
            island += 1

# 다리 구축
for x in range(N):
    for y in range(N):
        if world[x][y]:
            mini = min(mini, bridge(x, y, world[x][y]))

print(mini)