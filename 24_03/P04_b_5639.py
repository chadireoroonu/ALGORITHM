import sys
# 재귀호출 깊이 제한 설정
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("../temp/input.txt")


# 후위 순회 재귀 함수
def sol(root, end):
    # 더 이상 탐색할 노드가 없을 때
    if root > end:
        return

    # 현재 노드 값 저장
    temp = nums[root]
    # 루트 노드보다 큰 값이 나오는 인덱스
    big = end + 1

    # 루트 노드보다 큰 값 찾기
    for i in range(root + 1, end + 1):
        if temp < nums[i]:
            big = i
            break

    # 왼쪽 서브트리 재귀 함수 싫행
    sol(root + 1, big - 1)
    # 오른쪽 서브트리 재귀 함수 실행
    sol(big, end)
    # 현재 노트 출력
    print(nums[root])


# 입력 처리
nums = []
while True:
    try:
        num = int(sys.stdin.readline())
    except:
        break
    nums.append(num)

sol(0, len(nums) - 1)
