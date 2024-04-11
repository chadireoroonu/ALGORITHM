import sys, heapq
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
lectures = []  # 강의 정보
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    lectures.append([s, e])
lectures.sort()  # 강의 시간 정렬

maxi = 0  # 최대 강의실 수
rooms = []  # 사용하는 강의실 강의 종료 시간
for s, e in lectures:
    if rooms and s >= rooms[0]:
        heapq.heappop(rooms)
    # 현재 강의 정보 저장
    heapq.heappush(rooms, e)
    # 강의실의 수 재할당
    maxi = max(maxi, len(rooms))

print(maxi)
