# 실습 문제 03
# 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는 인덱스를 출력하라.
def main():
    a = input_list()
    while True:
        try:
            find = int(input('탐색할 정수를 입력하세요.: '))
            break
        except ValueError:
            print('정수가 아닌 값을 입력받았습니다.')
    linear_search(a, find)
    lsearch_s(a, find)

def linear_search(a, find): # 리스트 a를 선형탐색을 이용하여 검색.
    for i in range(len(a)):
        if a[i] == find:
            return i
    return -1 # 탐색 실패 시 -1를 반환.

def lsearch_s(a, find): # 보초법을 이용한 선형탐색.
    LIST = a.copy()
    LIST.append(find)
    index = 0
    while True:
        if LIST[index] == find:
            break
        else: index += 1
    return -1 if index >= len(a) else index

#def binary_search(a, find, prev, next): # 이진 탐색.
# 이진 탐색의 경우 sort를 해야하므로 문제의 취지에 부적합하다고 판단. 다른 code에서 연습. 
    
if __name__ == "__main__":
    main()


def input_list():
    LIST = []
    print('리스트에 들어갈 정수를 입력하세요.\n정수가 아닌 값을 입력하면 종료됩니다.: ', end='')
    try:
        while True:
            x = int(input())
            LIST.append(x)
    except ValueError: # 정수가 아닌 값을 입력받을 경우 예외 처리.
        return LIST