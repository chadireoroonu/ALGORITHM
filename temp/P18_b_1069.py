# 2차원 배열 visited 만들기
# BFS 이동
# 이동 시, 대각선 방향의 이동 가능 여부 생각하기
# 0, 0 도착 시 시간 출력

import sys
sys.stdin = open('input.txt')

X, Y, D, T = map(int, sys.stdin.readline().split())
