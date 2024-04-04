import sys
sys.stdin = open("../temp/input.txt")

# strip() : 개행문자 제거
string = sys.stdin.readline().strip()
target = list(map(str, sys.stdin.readline().strip()))
N = len(target)
stack = []

for alphabet in string:
    # string 한글자씩 stack 추가
    stack.append(alphabet)
    # stack 마지막 N 글자가 target과 같으면 N만큼 요소 삭제
    if len(stack) >= N and stack[-N:] == target:
        for _ in range(N):
            stack.pop()

# 리스트에 있는 것들 모아 출력
print(''.join(stack) if stack else "FRULA")
