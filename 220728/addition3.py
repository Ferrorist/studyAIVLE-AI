#추가 실습 03
# https://programmers.co.kr/learn/courses/30/lessons/77884
import math
def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, int(math.sqrt(i))+1):
          # 짝수의 경우 제곱근을 제외하면 서로 짝을 이룬다.
          # ex) 12일 경우, (1, 12), (2, 6), (3, 4)
          # 1,2,3의 경우 12의 제곱근보다 작으므로,
          # 제곱근보다 작거나 같은 정수만 탐색을 진행하면 된다. 
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

left, right = map(int, input().split())
# left = int(input())
# right = int(input())
print(solution(left, right))