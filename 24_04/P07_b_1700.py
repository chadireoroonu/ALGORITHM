# 아이디어
# 비어있는 플러그가 있다면 그냥 꽂기
# 비어있는 플러그가 없다면 다음 사용 순서 비교
#   다음 사용이 없는 것 뽑기
#   다음 사용이 가장 먼 것 뽑기, result += 1

import sys
sys.stdin = open("../temp/input.txt")

N, K = map(int, sys.stdin.readline().split())
electronics = list(map(int, sys.stdin.readline().split()))
order = [[] for _ in range(K + 1)]  # 사용되는 순서
result = 0

for i in range(K):
    order[electronics[i]].append(i)

plugs = set()
for electronic in electronics:
    order[electronic].pop(0)  # 사용 제품 제거
    if electronic in plugs:  # 이미 연결되어 있는 제품이면 무시
        continue
    if len(plugs) == N:  # 플러그에 빈 자리가 없는 경우
        target = 0  # 삭제 대상
        time = 0
        for x in plugs:
            # 사용이 끝난 제품이 있을 경우
            if not order[x]:
                target = x
                time = float('inf')
            # 남은 사용 시간이 가장 긴 것, 사용 시간이 같다면 출현 빈도가 적은 것 삭제
            elif order[x][0] > time:
                target = x
                time = order[x][0]
        # 플러그를 뽑고 result 더하기
        plugs.remove(target)
        result += 1
    plugs.add(electronic)

print(result)
