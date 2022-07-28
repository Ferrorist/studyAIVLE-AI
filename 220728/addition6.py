# 추가 실습 06
# https://programmers.co.kr/learn/courses/30/lessons/12934
import math
def solution(n):
    x = int(math.sqrt(n)) # x를 n의 제곱근의 정수부분으로 변경.
    if n == x**2: # x가 정수라면 x**2 = n이 나와야 한다.
        return (x+1)**2
    else:
        return -1

print(solution(int(input())))