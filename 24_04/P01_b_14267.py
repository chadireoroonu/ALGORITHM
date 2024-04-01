import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("../temp/input.txt")


# 내 자식들에게 나의 칭찬 점수 누적합산
def DFS(x):
    for nx in tree[x]:
        result[nx] += result[x]
        DFS(nx)
    return


n, m = map(int, sys.stdin.readline().split())
parents = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(n + 1)]  # 자식 정보
result = [0] * (n + 1)  # 칭찬 점수

# 자식 정보 기록
for i in range(1, n):
    tree[parents[i]].append(i + 1)

# 나의 칭찬 점수 계산
for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    result[i] += w

# 각 자식 탐색하며 칭찬 점수 누적
DFS(1)

# 0 인덱스 삭제 후 출력
result = result[1::]
print(*result)
