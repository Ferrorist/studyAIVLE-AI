# 추가 실습 06
# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    LIST = arr.copy()
    LIST.remove(min(LIST)) # 리스트의 최소값을 제거
    return LIST if len(LIST) > 0 else [-1] # LIST가 빈 배열이라면 [-1] return.

arr = [4,3,2,1]
print(solution(arr))