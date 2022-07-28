# 추가 실습 06
# https://programmers.co.kr/learn/courses/30/lessons/12934
import math
def solution(n):
    x = int(math.sqrt(n))
    if n == x**2:
        return (x+1)**2
    else:
        return -1

print(solution(int(input())))