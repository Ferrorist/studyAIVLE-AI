# 추가 실습 05
# 자연수 2개의 중복 가능한 자연수 집합
def solution(s):
    a = s//2
    if not a: 
        return [-1]
    left = s%2 # 0 또는 1
    LIST = []
    for _ in range(2): 
        num = a+1 if left > 0 else a # left가 남아있다면 원소 하나에 +1
        LIST.append(num)
        left -= 1
        # 두 자연수의 차이가 적을수록 곱하였을 때 큰 값이 나온다.
    LIST.sort()
    return LIST