def max3(a, b, c):
    maximum = a if (a > b) else b if (b > c) else c
    return maximum

print('정수의 최대값을 구합니다.')
a = int(input('정수 a의 값을 입력하시오. :'))
b = int(input('정수 b의 값을 입력하시오. :'))
c = int(input('정수 c의 값을 입력하시오. :'))

# maximum = a
# if b > maximum:
#     maximum = b
# if c > maximum:
#     maximum = c

#maximum = a if (a > b) else b if (b > c) else c
print(f'최대값은 {max3(a,b,c)}입니다.')