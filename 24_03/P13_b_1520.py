import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("../temp/input.txt")


def sol(i, j):
    # 목적지 도착 시 1 반환
    if i == N - 1 and j == M - 1:
        return 1

    # 방문한 적이 있다면 dp[i][j] 반환
    if dp[i][j] != -1:
        return dp[i][j]

    # 방문여부 표시
    dp[i][j] = 0
    # 상하좌우 탐색
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        # world 배열안에 있고, 현재값보다 작은 값에 대해 재귀 탐색
        if 0 <= ni < N and 0 <= nj < M:
            if world[i][j] > world[ni][nj]:
                # 목적지에 가는 모든 경로의 수 더하기
                dp[i][j] += sol(ni, nj)
    # 현재 위치에서 목적지에 가는 경로의 수 반환
    return dp[i][j]


N, M = list(map(int, sys.stdin.readline().split()))
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

print(sol(0, 0))
