import sys, heapq
sys.stdin = open("../temp/input.txt")

def djikstra(num):
    visited[num] = 0
    queue = []
    heapq.heappush(queue, [0, num])

    while queue:
        cost, now = heapq.heappop(queue)

        if cost <= visited[now]:
            for add, next in bus[now]:
                if visited[next] > cost + add:
                    visited[next] = cost + add
                    previous[next] = now
                    heapq.heappush(queue, [cost + add, next])
    return

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[] for _ in range(n + 1)]
visited = [int(1e9) for _ in range(n+1)]
previous = [-1 for _ in range(n + 1)]

for _ in range(m):
    s, e, v = list(map(int, sys.stdin.readline().split()))
    bus[s].append([v, e])

start, end = list(map(int, sys.stdin.readline().split()))

djikstra(start)
result = [end]

print(visited[end])

while end != start:
    end = previous[end]
    result.append(end)

print(len(result))

for i in result[::-1]:
    print(i, end=" ")
