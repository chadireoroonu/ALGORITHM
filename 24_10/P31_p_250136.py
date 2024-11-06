from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    oil = [0]*len(land[0]) # 세로 방향 석유 양 기록용
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 탐색 방향 지표
    
    for i in range(N):
        for j in range(M):
            if land[i][j]: # 석유 발견
                mini = maxi = j # 매장지 가로 길이 기록
                count = 0 # 석유 매장양
                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        # 다음 탐색지가 유효한 땅이며 석유 매장지일 경우
                        if 0 <= nx < N and 0 <= ny < M and land[nx][ny]:
                            count += 1
                            land[nx][ny] = 0
                            queue.append((nx, ny))
                            # 현재 매장지 y좌표로 mini, maxi 비교
                            mini = ny if mini > ny else mini
                            maxi = ny if maxi < ny else maxi
                # 석유 매장지 j 좌표에 매장량 추가
                for l in range(mini, maxi + 1):
                    oil[l] += count if count else 1
	# 세로 방향 최대 매장지
    answer = max(oil)             
    return answer