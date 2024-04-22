import sys
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
fluid = list(map(int, sys.stdin.readline().split()))
fluid.sort()  # 용액 정렬

# 투포인터 알고리즘을 위한 초기 설정
front = 0
rear = N - 1
total = float('inf')

while front < rear:
    # 두 인덱스 용액의 합
    temp = fluid[front] + fluid[rear]
    # 저장된 절댓값보다 현재 용액의 합 절댓값이 작은 경우
    if abs(total) > abs(temp):
        total = temp
        # 인덱스 저장
        ridx, lidx = front, rear
    # 현재 용액의 합이 음수인 경우 front 이동
    elif temp < 0:
        front += 1
    # 현재 용액의 합이 양수인 경우 rear 이동
    else:
        rear -= 1

# 저장된 두 인덱스의 용액 출력
print(fluid[ridx], fluid[lidx])
