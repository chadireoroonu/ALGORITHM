import sys
sys.stdin = open('input.txt')

# 연결 확인 함수
def check(m):
    if m != parent[m]:
        parent[m] = check(parent[m])
    return parent[m]

n = int(sys.stdin.readline().strip())
star = []
road = []
result = 0

# 별 정보 추가
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    star.append((x, y))

# 별 사이 거리 추가
for i in range(n-1):
    for j in range(i+1, n):
        road.append((((star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2) ** (1/2), i, j))

road.sort()
parent = [i for i in range(n)]

# 거리가 가까운 순으로 별자리 연결
for i in range(len(road)):
    e, x, y = road[i]
    if x < y:
        x, y = y, x
    if check(x) != check(y):
        parent[check(y)] = check(x)
        result += e

print(round(result, 2))