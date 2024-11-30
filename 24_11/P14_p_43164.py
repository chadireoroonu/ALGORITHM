def solution(tickets):
    answer = []
    visited = [False] * len(tickets) # 방문여부
    
    def DFS(route):
    	# 모든 티켓을 사용했다면 route에 경로 추가
        if len(route) == len(tickets) + 1:
            answer.append(route)
            return
            
 	    # 현재 위치에서 이동 가능한 곳으로 티켓 사용
        for i in range(len(tickets)):
            if tickets[i][0] == route[-1] and not visited[i]:
                visited[i] = True # 티켓 사용 표시
                DFS(route + [tickets[i][1]]) # 다음 목적지 추가
                visited[i] = False
        return
    
    DFS(['ICN'])
    answer = min(answer) # 알파벳순으로 가장 빠른 경로
    
    return answer