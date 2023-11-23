import sys
sys.stdin = open('../temp/input.txt')

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
x, y = list(map(int, sys.stdin.readline().split()))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
flag = False
visited = [[False] * 5 for _ in range(5)]

def DFS(i, j, depth, apple):
    global flag
    visited[i][j] = True
    if board[i][j] == 1:
        apple += 1
    if apple == 2:
        flag = True
        return
    if depth > 2:
        return
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5:
            if board[ni][nj] != -1 and not visited[ni][nj]:
                DFS(ni, nj, depth + 1, apple)
                visited[ni][nj] = False

DFS(x, y, 0, 0)

if flag:
    print(1)
else:
    print(0)