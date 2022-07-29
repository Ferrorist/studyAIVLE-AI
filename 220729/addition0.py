# 추가 실습 00 
# https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())
data = list(map(int, input().split()))
LIST = []
for i in data:
    if i < X:
        LIST.append(i)

for i in LIST:
    print(i, end=' ')