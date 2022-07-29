# 실습 02
# 리스트를 사용자로부터 입력받아서 역순으로 정렬하여 리스트의 원소를 출력하라.
# 단, 원소 수를 사용자에게 입력받지 않고 코드가 실행될 수 있게 만들어라.
def reverse_list(a):
    LIST = a.copy() # 깊은 복사
    n = len(LIST)
    for i in range(n//2):
        LIST[i], LIST[n-i-1] = LIST[n-i-1] , LIST[i]
    return LIST

def input_list():
    LIST = []
    print('리스트에 들어갈 정수를 입력하세요.\n정수가 아닌 값을 입력하면 종료됩니다.: ', end='')
    try:
        while True:
            x = int(input())
            LIST.append(x)
    except ValueError: # 정수가 아닌 값을 입력받을 경우 예외 처리.
        return LIST
        
a = input_list()
ra = reverse_list(a)
print(f'리스트의 역수를 출력합니다.\n{ra}')