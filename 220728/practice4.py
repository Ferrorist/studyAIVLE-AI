#실습 04
INPUT = int(input())
values = []
for i in range(1, INPUT+1):
    for j in range(2, 6): # 1 < pwr < 6
        if i**j == INPUT:
            values.append((i,j)) # (root, pwr) 형태의 tuple을 list에 저장.
        elif i**j > INPUT: break
        
if len(values) > 0:
    for i in range(len(values)):
        print(f'{values[i][0]}, {values[i][1]}')
else:
    print('결과 없음')