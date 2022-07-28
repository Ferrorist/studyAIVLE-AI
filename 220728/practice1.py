def electricPay(n):
    primary = 410
    cost = 0;
    if n < 100:
        cost = 60.7*n;
    else:
        cost += 60.7*100;
        if n > 200:
            primary = 1600
            cost += (125.9*100) + (187.9*(n-200))
        else:
            primary = 9102
            cost += 125.9*(n-100);
    return primary+cost

electric = int(input('사용 전력량을 입력하세요.: '))
price = electricPay(electric)
price += price * 0.137
print(int(price))