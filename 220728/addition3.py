#추가 실습 03
# https://programmers.co.kr/learn/courses/30/lessons/77884
import math
def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, int(math.sqrt(i))+1):
           if i%j == 0:
              if j**2 == i:
                count += 1
              else:
                count += 2
        if count%2==0:
            sum += i
        else:
            sum -= i
    return sum

left = int(input())
right = int(input())
print(solution(left, right))