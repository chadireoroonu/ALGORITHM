import sys
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))

front = 0
rear = N - 1

numL = liquid[front]
numR = liquid[rear]
mini = abs(numL + numR)

while front < rear:
    temp = liquid[front] + liquid[rear]
    if abs(temp) < mini:
        numL = liquid[front]
        numR = liquid[rear]
        mini = abs(temp)

        if temp == 0:
            break

    if temp < 0:
        front += 1

    else:
        rear -= 1

print(numL, numR)