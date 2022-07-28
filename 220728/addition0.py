# 추가 실습 00
# 두 정수의 최대공약수를 구하라. 최대공약수는 두 정수를
# 나머지가 0이 되게 나누는 공통된 약수 중 최대값을 가진 수이다.
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b:
        return gcd(b, a%b)
    else:
        return b

a, b = map(int, input().split) # 50 10 방식으로 입력 받음.
print(gcd(a,b))