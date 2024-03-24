import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
board = [[2] * 19 for _ in range(19)]
flag = False

for n in range(1, N + 1):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = n % 2

    # 오목 검사
    # 양방향 BFS

if not flag:
    print(-1)