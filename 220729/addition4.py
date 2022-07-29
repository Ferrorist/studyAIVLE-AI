# 실습 문제 04
# https://programmers.co.kr/learn/courses/30/lessons/12953
# 유클리드 호제법 활용
def gcd(a, b): # 최대공약수
    if b > a:
        a, b = b, a
    return gcd(b, a%b) if a%b else b

def lcm(a, b): # 최소공배수
    return abs(a*b)/gcd(a,b)


def solution(arr):
    answer = 1
    for num in arr:
        answer = lcm(answer, num)
    return answer

# arr = [2,6,8,14]
# answer = solution(arr)
# print(answer)