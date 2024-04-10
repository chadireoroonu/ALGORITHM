# 무게추의 무게 만큼 가능한 무게가 수가 늘어난다.
# 1
# + 1 : 1 2
# + 2 : 1 2 3 4
# + 3 : 1 2 3 4 5 6 7
# + 5 : 1 2 3 4 5 6 7 8 9 10 11 12
# num + 무게추 무게를 반복하다가, num < weight 순간 찾기

import sys
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
weights.sort()

num = 1  # 만들 수 없는 최소 숫자 초기 설정
# 모든 무게추의 무게를 더하며 num < weight 찾기
for weight in weights:
    if num < weight:
        break
    # 만들 수 있는 무게 정보 재할당
    num += weight

print(num)
