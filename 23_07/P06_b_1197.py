import sys
sys.stdin = open('input.txt')

# 루트 찾기 함수
def check(num):
    if parent[num] != num:
        parent[num] = check(parent[num])
    return parent[num]

V, E = map(int, sys.stdin.readline().split())

parent = [i for i in range(V+1)]
queue = []
result = 0

# 가중치 기준으로 연결 정보 정렬
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    queue.append([c, a, b])

queue.sort()

for i in range(len(queue)):
    x, y = queue[i][1], queue[i][2]
    # 연결 조건 통일
    if x < y:
        x, y = y, x
    # 루트 노드가 다를 때 연결
    if check(x) != check(y):
        parent[check(y)] = check(x)
        result += queue[i][0]

print(result)
