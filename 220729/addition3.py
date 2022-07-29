# 추가 실습 03
def solution(store, customer):
    answer = []
    for i in customer:
        exist = 'yes' if i in store else 'no'
        answer.append(exist)
    return answer

# store = [2,3,7,8,9]
# customer = [7,5,9]
# answer = solution(store, customer)
# print(answer)