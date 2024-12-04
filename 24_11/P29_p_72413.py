import heapq

def solution(n, s, a, b, fares):
    answer = int(1e9)
    road = [[] for _ in range(n + 1)]
    
    # 최소비용 탐색
    def djikstra(start):
        visited = [int(1e9)] * (n + 1)
        visited[start] = 0
        queue = []
        heapq.heappush(queue, [0, start])
        
        while queue:
            cost, now = heapq.heappop(queue)
            if cost <= visited[now]:
                for add, after in road[now]:
                    if visited[after] > cost + add:
                        visited[after] = cost + add
                        heapq.heappush(queue, [cost + add, after])
                            
        return visited
    
    
    # 입력 처리
    for i in range(len(fares)):
        start, end, cost = fares[i]
        road[start].append([cost, end])
        road[end].append([cost, start])
    
    # 출발지에서 모든 도착지까지 최소 비용 탐색
    together = djikstra(s)
    
    # 각 도착지에서 A,B 최소 비용 탐색
    for i in range(1, n + 1):
        route = djikstra(i)
        answer = min(together[i] + route[a] + route[b], answer)
    
    return answer