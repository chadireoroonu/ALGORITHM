import sys
sys.stdin = open("../temp/input.txt")

n = int(sys.stdin.readline())
count = 0  # 연산 횟수
cards = []
order = [[] for _ in range(n)]  # 각 카드 등장 순서
if n:
    cards = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    order[cards[i]].append(i)

boxes = set()
for card in cards:
    order[card].pop(0)  # 카드 사용 처리
    if card in boxes:  # 이미 상자에 있는 수 무시
        continue
    if len(boxes) == 4:  # 상자가 가득 찬 경우
        target = 0
        time = 0
        # 사용이 끝난 공, 가장 나중에 재사용할 공 탐색
        for ball in boxes:
            if not order[ball]:
                target = ball
                time = float('inf')
            elif order[ball][0] > time:
                target = ball
                time = order[ball][0]
        boxes.remove(target)  # 선정된 공 제거
    boxes.add(card)  # 상자에 공 추가
    count += 1  # 연산 횟수 증가

print(count)
