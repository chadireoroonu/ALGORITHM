import sys, heapq
sys.stdin = open("../temp/input.txt")

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    mini, maxi = [], []
    visited = [False] * 1000001
    for i in range(k):
        A, N = list(sys.stdin.readline().split())
        # 추가 연산 처리
        if A == 'I':
            # visited[i] 사용으로 향후 삭제 연산 대비
            heapq.heappush(mini, [int(N), i])
            heapq.heappush(maxi, [-int(N), i])
            visited[i] = True
        # 최솟값 삭제 연산 처리
        elif A == "D" and int(N) < 0:
            # 삭제 여부 visited 배열로 파악
            while mini and not visited[mini[0][1]]:
                heapq.heappop(mini)
            if mini:
                # 삭제 요소 visited 처리 및 최소힙에서 제거
                visited[mini[0][1]] = False
                heapq.heappop(mini)
        # 최댓값 삭제 연산 처리
        else:
            while maxi and not visited[maxi[0][1]]:
                heapq.heappop(maxi)
            if maxi:
                # 삭제 요소 visited 처리 및 최대힙에서 제거
                visited[maxi[0][1]] = False
                heapq.heappop(maxi)

    # 힙이 존재하며 visited 요소 false인 동안 반복
    while mini and not visited[mini[0][1]]:
        heapq.heappop(mini)
    while maxi and not visited[maxi[0][1]]:
        heapq.heappop(maxi)

    if mini and maxi:
        print(-maxi[0][0], mini[0][0])
    else:
        print("EMPTY")

# 25%, 68%