import sys
from collections import deque
sys.stdin = open('input.txt')

def cycle(n):
    temp = 1
    queue = deque()
    queue.append(students[n])
    visited = [0]*N
    visited[students[n]-1] = 1
    while queue:
        j = queue.popleft()
        nj = students[j-1]
        if nj == n:
            return temp + 1
        if not visited[nj]:
            visited[nj] = 1
            queue.append(nj)
            temp += 1
    return 0

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    num = 0

    for i in range(N):
        if students[i] == i + 1:
            num += 1
        elif students[i]:
            num += cycle(i)

    print(N-num)