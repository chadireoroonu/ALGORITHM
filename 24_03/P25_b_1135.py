import sys
sys.stdin = open("../temp/input.txt")


def dp(n):
    # 이전에 검사한 적이 있다면 검사 결과 반환 종료
    if time[n] > -1:
        return time[n]

    # 해당 노드의 자식이 없다면 0 저장 후 0 반환 종료
    if not children[n]:
        time[n] = 0
        return 0

    # 모든 자식 노드 방문 소요 시간 계산
    temp = [dp(child) for child in children[n]]

    if temp:  # 자식노드가 있다면 내림차순 정렬
        temp.sort(reverse=True)

        # 방문 순서에 따른 추가 시간 반영
        for idx, t in enumerate(temp):
            temp[idx] = idx + t

        # temp 최고값에 현재 노드 방문 시간 반영
        time[n] = max(temp) + 1
        return time[n]


N = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
children = [[] for _ in range(N)]  # 자식 정보 배열
time = [-1] * N  # 누적시간 저장

# 자식 정보 저장
for i in range(N):
    if parent[i] >= 0:
        children[parent[i]].append(i)

# 시간 탐색
for i in range(N):
    dp(i)

# 루트 노드의 시간 출력
print(time[0])
