# 추가 실습 05-1 [프로그래머스]
# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s): # n개의 자연수의 합이 s {1,1,1,1,1,1}
    if s//n == 0: 
        # n개의 자연수의 합이 최소값은 n이다.
        # s//n이 0이라면 s는 n보다 작은 것이다. 즉, 문제에서 제시한 집합이 존재할 수 없다.
        return [-1]
    a = s//n; left = s%n
    LIST = []
    for _ in range(n):  
        num = a+1 if left > 0 else a
        LIST.append(num)
        left -= 1
    LIST.sort()
    return LIST
    

print(solution(10,45))