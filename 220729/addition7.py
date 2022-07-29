# 추가 실습 07
# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    LIST = []
    data = arr[0]
    LIST.append(data)

    for i in range(1, len(arr)):
        if arr[i] != data:
            data = arr[i]
            LIST.append(data)
    return LIST

arr = [1,1,3,3,0,1,1]
print(solution(arr))