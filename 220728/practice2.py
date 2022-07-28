# 실습 02
count = int(input('+와 -를 번갈아 출력합니다.\n몇 개를 출력할까요? '))
for i in range(count):
    if i%2==0:
        print('+', end='')
    else:
        print('-', end='')
print()