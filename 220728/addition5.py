# 추가 실습 05
# https://www.acmicpc.net/problem/18406
def lucky(n):
    score = str(n)
    mid = int(len(score)/2)
    left = 0
    right = 0
    for i in range(mid):
        left += int(score[i])
    for i in range(mid, len(score)):
        right += int(score[i])
    
    if left == right:
        return "LUCKY"
    else:
        return "READY"

print(lucky(int(input())))