import sys
from collections import deque
sys.stdin = open("../temp/input.txt")


def sol(n, m):
    # m이 n의 부모라면 m 출력
    if parent[n] == m:
        return print(m)

    # n의 자식들의 자식들을 찾아나가며 m 찾기
    queue = deque([n])
    while queue:
        x = queue.popleft()
        for y in tree[x]:
            # m 발견 시 return
            if y == m:
                return print(n)
            queue.append(y)

    # n 대신 n 부모 노드로 재귀 호출
    sol(parent[n], m)


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    # 자식 정보, 부모 정보 저장
    tree = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = list(map(int, sys.stdin.readline().split()))
        tree[A].append(B)
        parent[B] = A

    a, b = list(map(int, sys.stdin.readline().split()))

    sol(a, b)