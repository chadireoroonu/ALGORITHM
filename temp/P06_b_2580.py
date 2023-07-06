import sys
from collections import deque
sys.stdin = open('input.txt')

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
sell = deque()

for x in range(9):
    for y in range(9):
        if not paper[x][y]:
            sell.append((x, y))

print(paper)

while sell:
    queue = deque()
    for t in range(1, 10):
        queue.append(t)
    print(queue)
    i, j = sell.popleft()
    # 후보 숫자 찾기
    for t in range(9):
        queue.remove(paper[i][t])
        print(queue)
        try:
            queue.remove(paper[t][j])
        except:
            pass

    # 숫자 확정 가능 시 채우기
    # 불가능 시 큐 맨 뒤로 이동
