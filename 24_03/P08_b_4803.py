import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

# 사이클 여부 확인
def iscylcle(num):
    global parent
    queue = deque([num])
    visited = [False] * (n + 1)
    while queue:
        # x 방문 전적이 있다면 사이클
        x = queue.popleft()
        if visited[x]:
            return 0
        visited[x] = True
        # x와 연결된 노드 검사
        for nx in tree[x]:
            # 검사 여부
            check[nx] = False
            # 방문하지 않았던 연결 노트 queue 추가
            if not visited[nx]:
                queue.append(nx)
    return 1

# 테스트 케이스
tc = 0
while True:
    n, m = list(map(int, sys.stdin.readline().split()))
    tc += 1
    # 입력이 0 0 일 경우 종료
    if n == 0:
        break
    # 사이클 검사 수행 여부
    check = [True] * (n + 1)
    # 연결 정보
    tree = [[] for _ in range(n + 1)]
    # 트리 수
    count = 0

    # 입력
    for _ in range(m):
        s, e = list(map(int, sys.stdin.readline().split()))
        if s > e:
            s, e = e, s
        tree[s].append(e)
        tree[e].append(s)

    # 사이클 검사 미수행 노드에 대해 함수 실행
    for i in range(1, n + 1):
        if check[i]:
            if iscylcle(i):
                count += 1

    # 출력
    if not count:
        print(f'Case {tc}: No trees.')
    elif count == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {count} trees.')