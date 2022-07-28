# 중앙값 찾기.
def medium(list = []):
    count = len(list)
    if count%2 != 0:
        return list[int(count/2)]
    else:
        index = int(count/2)
        return (list[index-1] + list[index])/2


Integer = []

print('입력된 정수의 중앙값을 찾습니다.\n음수가 입력될 경우 입력을 정지합니다.')
while True:
    a = int(input())
    if a < 0:
        print('입력을 중단합니다.')
        break
    Integer.append(a)
    
Integer.sort()
print(f'중앙값은 {medium(Integer)}입니다.')
