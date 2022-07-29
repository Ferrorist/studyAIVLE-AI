# 실습 01
# 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하라.

def eratosthenes(max): # 1부터 max까지의 에라토스테네스의 체 return.
    LIST = [False, False] + [True] * (max-1)
    # LIST[i] = 'i가 소수인가?'에 대한 boolean 값. True : 소수. False : 소수가 아님.
    # 0, 1은 소수가 아니므로 False를 이외의 값은 탐색 전에 True로 초기화. max index까지 탐색을 진행할 것이다.
    for i in range(2, max+1):
        if LIST[i]: # i가 소수일 때 실행.
            for j in range(i*2, max+1, i):
                LIST[j] = False # i의 배수는 소수가 아니므로 False로 변환.
    return LIST # 에라토스테네스의 체 return

def get_prime(max):
    sieve = eratosthenes(max) # 체를 생성
    LIST = []
    for i in range(len(sieve)):
        if sieve[i]: # 체를 확인하여 True값일 경우 list에 append
            LIST.append(i)
    return LIST

# while True:
#     Integer = int(input('2부터 소수를 탐색합니다.\n몇 까지 탐색할까요? '))
#     if Integer < 2:
#         print('2보다 작은 값을 입력받았습니다. 다시 입력바랍니다.')
#         continue
#     else: break

primes = get_prime(1000)
print(primes)