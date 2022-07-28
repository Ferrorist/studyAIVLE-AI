#추가 실습 01
# 두 정수의 최소공배수를 구하라.
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b:
        return gcd(b, a%b)
    else:
        return b

def lcm(a, b):
    return int((a*b)/gcd(a,b))

a, b = map(int, input().split())
print(lcm(a,b))