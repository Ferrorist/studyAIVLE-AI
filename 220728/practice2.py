# 실습 02
count = int(input('+와 -를 번갈아 출력합니다.\n몇 개를 출력할까요? '))
plus = True
for _ in range(count):
    if plus:
        print('+', end='')
    else:
        print('-', end='')
    plus = False if plus else True
print()