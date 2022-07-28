# 추가 실습 02
# 백준 1110번. 더하기 사이클
# https://www.acmicpc.net/problem/1110
def cycle(n):
    number = n
    count = 0
    while True:
        if number < 10:
            number *= 11
            count += 1
        else:
            calc = number/10 + number%10
            number = int((number%10)*10 + calc%10)
            count += 1
        print(f'number = {number}')
        if number == n: break
    return count

n = int(input())
print(cycle(n))