# 실습 문제 04
# https://programmers.co.kr/learn/courses/30/lessons/12953
def gcd(a, b):
    if b > a:
        a, b = b, a
    return gcd(b, a%b) if a%b else b

def lcm(a, b):
    return abs(a*b)/gcd(a,b)


def solution(arr):
    answer = 1
    for num in arr:
        answer = lcm(answer, num)
    return answer

arr = [2,6,8,14]
answer = solution(arr)
print(answer)