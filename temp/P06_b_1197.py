import sys
from queue import PriorityQueue
from collections import deque
sys.stdin = open('input.txt')

V, E = map(int, sys.stdin.readline().split())
node = [[]for _ in range(V+1)]

for _ in range(E):
    a, b, p = map(int, sys.stdin.readline().split())
    node[a].append([p, b])
    node[b].append([p, a])

que = PriorityQueue()
used = deque()
