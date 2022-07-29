# 실습 문제 03
# 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는 인덱스를 출력하라.

def input_list():
    LIST = []
    print('리스트에 들어갈 정수를 입력하세요.\n정수가 아닌 값을 입력하면 종료됩니다.: ', end='')
    try:
        while True:
            x = int(input())
            LIST.append(x)
    except ValueError: # 정수가 아닌 값을 입력받을 경우 예외 처리.
        return LIST