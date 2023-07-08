import sys
sys.stdin = open('../temp/input.txt')

# 연결 확인 함수
def check(parent, n):
    if parent[n] != n:
        parent[n] = check(parent, parent[n])
    return parent[n]

# 오르막길 더하기 함수
def count(temp):
    parent = [i for i in range(N+1)]
    for j in range(M+1):
        x, y = check(parent, road[j][1]), check(parent, road[j][2])
        # 추가 조건 맞추기
        if x > y:
            x, y = y, x
        if x != y:
            parent[y] = x
            # 오르막길 카운트
            if not road[j][0]:
                temp += 1
    return temp

N, M = map(int, sys.stdin.readline().split())

maxi = mini = 0
road = []

for _ in range(M+1):
    a, b, c = map(int, sys.stdin.readline().split())
    road.append([c, a, b])

# maxi -> 오름차순 순회
road.sort()
maxi = count(maxi) ** 2

# mini -> 내림차순 순회
road.sort(reverse=True)
mini = count(mini) ** 2

print(maxi - mini)
