# 연결 정보 담고 정렬
# 앞에서부터 하나씩 뽑기
# 부모 노드 검사
# 부모 노드가 다르다면 두 노드 연결
# 연결 시 가중치 더하기

import sys
sys.stdin = open('input.txt')

V, E = map(int, sys.stdin.readline().split())
parent = [0] * (V+1)
queue = []
result = 0

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    queue.append([a, b, c])

queue.sort()


def check(n):
    if parent[n] and :

    return


for i in range(len(queue)):
    x = queue[i][1]
    y = queue[i][2]
    if x < y:
        x, y = y, x
    if check(x) and check(y) and check(x) != check(y):
        parent[y] = x
        result += queue[i][0]

print(result)
