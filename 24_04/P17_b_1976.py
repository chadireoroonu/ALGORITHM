import sys
sys.stdin = open("../temp/input.txt")


# 부모를 거슬러 올라가 루트 탐색
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 두 수의 루트 탐색 후 연결
def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        x, y = y, x
    parent[y] = x
    return


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]  # 초기 설정

for i in range(N):
    # 연결 정보 리스트
    loads = list(map(int, sys.stdin.readline().split()))
    # 각 도시와 연결되어 있다면 union 함수로 연결
    for j in range(N):
        if loads[j]:
            union(i + 1, j + 1)

route = list(map(int, sys.stdin.readline().split()))  # 여행할 도시들
temp = parent[route[0]]  # 여행 첫 도시의 부모
for city in route:
    # 부모가 다른 도시는 연결되지 않은 도시
    if parent[city] != temp:
        print('NO')
        break
else:  # 모든 도시가 연결되어 있는 경우
    print('YES')
