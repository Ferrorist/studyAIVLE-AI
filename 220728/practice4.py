#미니 실습 4
area = int(input('직사각형의 넓이를 입력하세요.: '))

angle = 2 if area%2==0 else 1;
# area가 짝수면 angle = 2, 홀수면 angle = 1
print(f'1 X {area}') # 1은 곱셈의 항등원이므로 제일 먼저 나오는 결과.

for i in range(angle, area+1, 2): # i가 2씩 증가함.
    if area%i == 0:
        print(f'{i} X {area//i}')