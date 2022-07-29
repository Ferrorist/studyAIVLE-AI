#import copy
# 미니 실습 02
def reverse_list(a):
#    LIST = copy.deepcopy(a) # 깊은 복사. import copy 필요.
    LIST = a.copy() # list.copy() 또한 깊은 복사가 가능하다.
    n = len(LIST)
    print('리스트를 역순으로 출력합니다.')
    for i in range(n//2):
        LIST[i], LIST[n-i-1] = LIST[n-i-1], LIST[i]
    return LIST
    

def make_list():
    LIST = []
    count = int(input('원소 수를 입력하세요.: '))
    for i in range(count):
        LIST.append(int(input(f'x[{i}]값을 입력하세요.: ')))
    return LIST

def print_list(a):
    for i in a:
        print(i)

a = make_list()
ra = reverse_list(a)
print_list(ra)