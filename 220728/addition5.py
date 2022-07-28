# 추가 실습 05
# https://www.acmicpc.net/problem/18406
def lucky(n):
    score = str(n) # 연산의 편의성을 위해서 문자열로 형변환.
    mid = int(len(score)/2) # 점수의 자릿수의 중간을 기준으로 계산하니까.
    left = 0
    right = 0
    for i in range(mid):
        left += int(score[i]) # 좌측 숫자 합
    for i in range(mid, len(score)):
        right += int(score[i]) # 우측 숫자 합
    
    if left == right:
        return "LUCKY"
    else:
        return "READY"

print(lucky(int(input())))