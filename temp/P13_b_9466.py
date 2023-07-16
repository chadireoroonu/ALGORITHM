import sys
from collections import deque
sys.stdin = open('input.txt')

def cycle(n):
    temp = 1
    queue = deque()
    queue.append(students[n-1])
    while queue:
        j = queue.popleft()
        nj = students[j - 1]
        if nj == n-1 and not visited[n-1]:
            return temp
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
    visited = [0]*(N+1)

    for i in range(N):
        if students[i] == i + 1:
            visited[students[i] - 1] = 1
            num += 1
        elif not visited[i]:
            visited[students[i] - 1] = 1
            num += cycle(i)

    print(N-num)