#미니 실습 4
area = int(input('직사각형의 넓이를 입력하세요.: '))

angle = 2 if area%2==0 else 1;
# area가 짝수면 angle = 2, 홀수면 angle = 1
if angle%2==0:
    print(f'1 × {area}') 
    # 1은 곱셈의 항등원이므로 제일 먼저 나오는 결과.
    # 아래의 for문이 2부터 시작을 한다면 1×n의 경우의 수가 출력되지 않는다.
    # 이러한 경우를 방지하고자 넣은 print()문이다.

for i in range(angle, area+1, 2): # i가 2씩 증가함.
    if area%i == 0:
        print(f'{i} × {area//i}')
