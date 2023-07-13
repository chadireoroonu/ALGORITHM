import sys
from collections import deque
sys.stdin = open('input.txt')

def cycle(n):
    temp = 1
    queue = deque()
    queue.append(students[n])
    while queue:
        j = queue.popleft()
        if students[j-1]:
            queue.append(students[j-1])
            print(f'n={n}, j={j}, students={students}')
            students[j-1] = 0
            temp += 1
        if j == n:
            return temp
    return 0

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    num = 0

    for i in range(N):
        if students[i] == i + 1:
            print(f'i={i}')
            students[i] = 0
            num += 1
        elif students[i]:
            num += cycle(i)

    print(N-num)