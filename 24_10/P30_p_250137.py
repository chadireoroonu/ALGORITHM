def solution(bandage, health, attacks):
    answer = health
    second = 0 # 붕대감기 지속 시간
    pointer = 0 # 다음 공격
    
    for i in range(attacks[-1][0] + 1):
    	# 공격을 받은 경우
        if i == attacks[pointer][0]:
            answer -= attacks[pointer][1]
            pointer += 1
            second = 0
            # 공격을 받아 죽은 경우
            if answer <= 0:
                answer = -1
                break
        else: # 공격 받지 않은 경우 붕대감기
            answer = min(answer + bandage[1], health)
            second += 1
            # 스킬 완료로 추가회복
            if second == bandage[0]:
                answer = min(answer + bandage[2], health)
                second = 0
              
    return answer