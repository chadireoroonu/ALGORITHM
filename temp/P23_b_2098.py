import sys, heapq
sys.stdin = open("input.txt")

def solution(n):
    queue = []
    visited = [int(1e9) for _ in range(N)]
    heapq.heappush(queue, [0, n])
    while queue:
        cost, x = heapq.heappop(queue)
        for j in range(N):
            add = load[x][j]
            if add and add + cost < visited[x]:
                visited[x] = add + cost
                heapq.heappush(queue, [cost + add, j])
    print(visited)
    return visited[n]

N = int(sys.stdin.readline())
load = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

money = 0

print(load)

for i in range(N):
    checked = [False for _ in range(N)]
    money += solution(i)

print(money)

