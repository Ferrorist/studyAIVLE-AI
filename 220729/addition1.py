# 추가 실습 01
# https://programmers.co.kr/learn/courses/30/lessons/77484

rank = [6,6,5,4,3,2,1] # rank[6] = 1 : 6개 다 맞추었으므로 1등

def solution(lottos, win_nums):
    zero = lottos.count(0) # lottos에서 0의 개수를 저장.
    count = 0
    for num in win_nums:
        if num in lottos: # win_nums가 lottos에 있을 경우 count++
            count += 1
    return rank[zero+count], rank[count]
    # rank[zero+count] : 0이 모두 당첨 숫자 -> 등수가 가장 높음.
    # rank[count] : 0이 모두 당첨 숫자가 아님 -> 등수가 가장 낮음.