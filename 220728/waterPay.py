# 미니 실습 2
# 다음은 A, B 두 수도 회사의 요금 체계이다.
# A : 1L 당 요금 100원,
# B : 50L 이하일 경우 1L 당 요금 150원, 50L 초과 시 1L당 75원
# 수도회사와 수도 사용량을 입력받아 지불해야 하는 수도 요금을 계산하는
# waterPay()를 만들고, 수도 회사와 수도 사용량을 입력받아 요금을 출력하라.
def waterPay(a, b):
    A = a * 100
    if b <= 50:
        B = b * 150
    else:
        B = b * 75
    return A, B

companyA = input('첫 번째 회사의 이름을 입력하세요. : ')
companyB = input('두 번째 회사의 이름을 입력하세요. : ')
A = int(input(f'{companyA}의 수도 사용량을 입력하세요. : '))
B = int(input(f'{companyB}의 수도 사용량을 입력하세요. : '))
costA, costB = waterPay(A, B)
print(f'{companyA}: {A}L\n요금:{costA}원')
print(f'{companyB}: {B}L\n요금:{costB}원')