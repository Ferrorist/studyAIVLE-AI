count = int(input())
if count <= 0:
    exit() # 정수 개수가 0 이하일 경우 실행하지 않음.
    # If the input value is less than or equal to 0, the program is not executed.
    
Integer = [] # 빈 리스트 생성.
for i in range(count):
    Integer.append(int(input()))

Integer.sort()
print(f'최대값은 {Integer[-1]}입니다.')