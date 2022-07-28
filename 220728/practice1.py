def electricPay(n):
    primary = 410
    cost = 0
    if n < 100:
        cost = 60.7*n
    else:
        cost += 60.7*100
        if n < 200:
            primary = 910
            cost += 125.9*(n-100)
        else:
            cost += 125.9*100
            primary = 1600
            cost += 187.9*(n-200)
    price = primary+cost
    price += price * 0.137 # 0.1(부가가치세 10%) + 0.037(전력산업기반기금 3.7%)
    return int(price)

electric = int(input('사용 전력량을 입력하세요.: '))
print(electricPay(electric))
