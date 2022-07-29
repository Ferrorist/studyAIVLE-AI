# 실습 문제 03 (이진 탐색 - 개인 연습용)
# 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는지를 판별하라.

def main():
    a = input_list()
    while True:
        try:
            find = int(input('탐색할 정수를 입력하세요.: '))
            break
        except ValueError:
            print('정수가 아닌 값을 입력받았습니다.')
    a.sort() # a.sort(reverse=True) : a를 내림차순으로 정렬
    result = binary_search(a, find, 0, len(a)-1)
    if result == -1:
        print('리스트에 없는 값입니다.')
    else:
        print('리스트에 존재하는 값입니다.')

def binary_search(a, find, prev, next): # 이진 탐색. 
    # prev : 탐색 범위의 첫번째 index, next : 탐색 범위의 마지막 index
    mid = (prev + next) // 2
    if a[mid] == find:
        return mid
    if prev == next: # prev와 next가 같으면 탐색 범위가 더 이상 존재하지 않는다는 것.
        return -1
    return binary_search(a, find, prev, mid) if a[mid] > find else binary_search(a,find, mid, next)
    
def input_list():
    LIST = []
    print('리스트에 들어갈 정수를 입력하세요.\n정수가 아닌 값을 입력하면 종료됩니다.: ', end='')
    try:
        while True:
            x = int(input())
            LIST.append(x)
    except ValueError: # 정수가 아닌 값을 입력받을 경우 예외 처리.
        return LIST

if __name__ == "__main__":
    main()
