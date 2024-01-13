import sys
sys.stdin = open("input.txt")

N, M = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N+1)]


# 부모 노드 찾기
def find(n):
    if parent[n] == n:
        return n
    else:
        return find(parent[n])


# 부모가 다를때 집합 합치기
def add(x, y):
    if find(x) > find(y):
        parent[find(y)] = find(x)
    else:
        parent[find(x)] = find(y)
    return


for i in range(M):
    r, a, b = list(map(int, sys.stdin.readline().split()))
    if r:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        add(a, b)