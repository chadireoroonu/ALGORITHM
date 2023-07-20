import sys
sys.stdin = open('input.txt')

# 조건 외 항 검사
def check(x, y):
    for i in range(N-1):
        if num[i] * x + y != num[i+1]:
            return print('B')
    return print(num[-1] * x + y)

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))

# 숫자가 2개 이하인 경우
if N <= 2:
    if N > 1 and num[0] == num[1]:
        print(num[0])
    else:
        print('A')
# 숫자가 3개 이상이면 a, b 구하기
else:
    if not num[1] - num[0]:
        a = 1
    else:
        a = (num[2] - num[1]) // (num[1] - num[0])
    b = num[1] - num[0] * a
    check(a, b)
