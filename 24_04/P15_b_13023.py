import sys
sys.stdin = open("../temp/input.txt")


# 한 숫자에서 다섯 번 DFS 호출이 가능한지 확인
def DFS(n, depth):
    visited[n] = True  # 방문표시
    if depth == 5:
        return 1  # 문제 조건 충족 종료
    # 연결된 친구들에 대해 이전에 확인하지 않았다면 DFS 호출
    for friend in friends[n]:
        if not visited[friend]:
            if DFS(friend, depth + 1):
                return 1  # 문제 조건 충족 전달
            visited[friend] = False  # 방문 초기화
    visited[n] = False  # 방문 초기화
    return 0


N, M = map(int, sys.stdin.readline().split())
friends = [[] for _ in range(N)]  # 친구관계 저장
visited = [False] * N

for _ in range(M):  # 친구관계 입력 받기
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(N):
    if DFS(i, 1):  # 문제 조건 충족 시
        print(1)
        break
else:
    print(0)  # 문제 조건 미충족 시
