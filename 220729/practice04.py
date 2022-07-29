# 실습 04
# 리스트를 사용자로부터 입력받아서 최대값과 최대값이 있는 인덱스를 출력하라.

def input_list():
    LIST = []
    print('리스트에 들어갈 정수를 입력하세요.\n정수가 아닌 값을 입력하면 종료됩니다.: ', end='')
    try:
        while True:
            x = int(input())
            LIST.append(x)
    except ValueError: # 정수가 아닌 값을 입력받을 경우 예외 처리.
        return LIST

# def find_max(a):
#     LIST = a.copy()
#     LIST.sort()
#     return LIST[-1]

a = input_list()
# a_max = find_max(a)
# for i in range(len(a)):
#     if a[i] == a_max:
#         print(f'최대값 {a_max}의 index : {i}')
#         break
print(f'최대값 {max(a)}의 index : {a.index(max(a))}')