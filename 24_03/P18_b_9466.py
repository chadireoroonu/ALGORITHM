import sys
from collections import deque
sys.stdin = open("../temp/input.txt")


# 사이클 확인
def iscycle(n):
    # 지목된 학생들
    team = dict()
    team[n] = 0
    queue = deque([(n, 0)])
    check[n] = True
    while queue:
        x, idx = queue.popleft()
        # 현재 학생이 지목한 학생
        nx = arrow[x]
        # 지목한 학생이 이미 팀에 있을 경우
        if nx in team:
            return len(team) - team[nx]
        # 지목된 학생이 팀에 없을 경우
        if not check[nx]:
            team[nx] = idx + 1
            queue.append((nx, idx + 1))
            check[nx] = True

    # 사이클이 아니면 0명 반환
    return 0


T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    # 지목하는 학생 정보
    arrow = [0] + list(map(int, sys.stdin.readline().split()))
    # 사이클 판별 여부
    check = [False] * (N + 1)
    # 팀을 이루지 못한 학생 수
    alone = N

    # 사이클로 판별되지 않은 학생에 대해 판별 함수 실행
    for i in range(1, N + 1):
        if not check[i]:
            # 전체 학생수에서 팀을 이룬 학생 수 차감
            alone -= iscycle(i)

    print(alone)
