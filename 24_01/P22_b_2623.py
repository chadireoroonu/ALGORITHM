import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

N, M = list(map(int, sys.stdin.readline().split()))

# 본인 이전 가수의 수
previousN = [0 for _ in range(N + 1)]

# 본인 이후 가수 번호
nextN = [[] for _ in range(N + 1)]

# 정답을 담을 queue
result = deque()

# 순서 탐색을 위한 queue
queue = deque()

# 입력
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    # 보조 PD 담당 수는 제외하고 인덱스 1부터 끝까지 정보 입력
    for i in range(1, len(temp) - 1):
        for j in range(i + 1, len(temp)):
            previousN[temp[j]] += 1
            nextN[temp[i]].append(temp[j])

# 이전 가수가 없으면 queue에 추가
for i in range(1, N + 1):
    if not previousN[i]:
        queue.append(i)

while queue:
    x = queue.popleft()
    # 출연 순서대로 result에 추가
    result.append(x)

    # 내 다음에 부를 가수들의 previous 값 줄이기
    for nx in nextN[x]:
        previousN[nx] -= 1
        # 더 이상 먼저나올 가수가 없다면 queue에 추가
        if not previousN[nx]:
            queue.append(nx)

# result의 길이가 N과 같아 모두 출연했다면 출연 순서대로 출력
if len(result) == N:
    while result:
        print(result.popleft())
else:
    print(0)