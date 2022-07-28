name = input('이름을 입력하세요: ')
print(f'안녕하세요? {name}님')
# f-string: f'(문자열) {변수} (문자열)' 형태로 선언. 변수 내용이 문자열에 포함됨.

length = input('정사각형의 한 변의 길이를 입력하세요.:')
print(f'정사각형의 넓이는 {int(length)**2}입니다.')
# input()의 입력값은 문자열. int()를 이용하여 형변환.