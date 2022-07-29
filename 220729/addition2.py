# 추가 실습 02
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    sum = 0
    for i in range(10):
        if i not in numbers:
            sum += i
    # return 45 - sum(numbers)
    # sum(iterable) : 인자로 전달되는 iterable의 합을 리턴.
    return sum