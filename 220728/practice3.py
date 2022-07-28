#실습 03
# 1부터 12까지를 for loop를 활용하여 출력하라. 단, 8은 건너뛰고 출력하라.
max = 12
for i in range(1, max+1):
    if i == 8: continue
    print(f'{i} ', end='')
print()