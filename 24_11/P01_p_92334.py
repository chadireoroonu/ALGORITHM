def solution(id_list, report, k):
    answer = [0] * len(id_list)
    count = [0] * len(id_list) // 신고당한 횟수
    complain = [[] for _ in range(len(id_list))] # 신고한 사람들
    
    # 신고정보 입력 처리
    for i in range(len(report)):
        r, t = map(str, report[i].split())
        
        # id_list의 인덱스로 이름을 숫자처럼 사용
        if t not in complain[id_list.index(r)]:
            complain[id_list.index(r)].append(t)
            count[id_list.index(t)] += 1
    
    # 내가 신고한 사람들의 신고 횟수 확인 및 기록
    for i in range(len(id_list)):
        for j in complain[i]:
            if count[id_list.index(j)] >= k:
                answer[i] += 1
    
    return answer