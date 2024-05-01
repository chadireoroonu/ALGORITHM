import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

N, M = map(int, sys.stdin.readline().split())
order = [1] * N  # 수강 가능한 학기
previous = [0] * (N + 1)  # 선수과목의 수
after = [[] for _ in range(N + 1)]  # 다음 과목

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    previous[B] += 1  # 선수과목 수 반영
    after[A].append(B)  # 다음 과목 정보 저장

# 선수과목이 없는 과목 queue 추가
queue = deque([i for i in range(1, N + 1) if not previous[i]])

while queue:
    x = queue.popleft()
    # 현재 과목 다음 과목들의 선수과목 수 조정
    for nx in after[x]:
        previous[nx] -= 1
        # 다음 과목의 모든 선수과목을 수강한 경우 학기 기록, queue 추가
        if not previous[nx]:
            order[nx - 1] = order[x - 1] + 1
            queue.append(nx)

print(*order)
