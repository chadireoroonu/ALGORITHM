import sys
sys.stdin = open("input.txt")

N = sys.stdin.readline()
M = sys.stdin.readline()
broken = list(map(int, sys.stdin.readline().split()))
now = 100
count = 0

