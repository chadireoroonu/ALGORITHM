import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

N, M, T = list(map(int, sys.stdin.readline().split()))
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 각 칸 도착 시간
gram = 0  # 그람 활용 목적지 도착 시간
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동방향

queue = deque()
queue.append((0, 0))  # 출발지
while queue:
    i, j = queue.popleft()
    time = visited[i][j]  # 현재까지 소요시간
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]  # 상하좌우 확인
        if 0 <= ni < N and 0 <= nj < M:
            # 그람 최초 발견 시, 그람 활용 도착 시간 저장
            if castle[ni][nj] == 2 and not gram:
                gram = time + N - ni + M - nj - 1
            else:
                # 벽이 없는 길 이동 시간 BFS 탐색
                if not visited[ni][nj] and not castle[ni][nj]:
                    visited[ni][nj] = time + 1
                    queue.append((ni, nj))

sol = visited[N - 1][M - 1]  # 도보로 목적지 도착 가능 시
if gram and sol:  # 그람, 도보 모두 목적지 도착 가능 시 작은 값 저장
    sol = gram if gram < sol else sol
elif gram and not sol:  # 그람으로만 목적지 도착 가능 시 저장 값 변경
    sol = gram

# 도착 시간이 0이 아니고 T보다 작을 때 출력, 조건 미충족 시 Fail 출력
print(sol if sol and sol <= T else "Fail")
