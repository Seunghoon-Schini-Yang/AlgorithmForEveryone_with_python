stock = [10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]

# O(n)
def max_profit(stock) :  # max profit 낼 수 있는 매수 매도 가격 구하기
    buy = stock[0]
    sell = stock[0]
    buy_w = stock[0]
    profit = sell - buy
    for i in range(1,len(stock)) :
        price = stock[i]
        if price > buy_w :
            if price - buy_w > profit :
                sell = price
                buy = buy_w
                profit = sell - buy
        else :
            buy_w = price
    print(buy,sell)

max_profit(stock)


# O(n^2)  # 모든 경우의 수 비교
def max_profit_double_for(stock) :
    max_pfit = 0
    for i in range(len(stock)-1) :
        for j in range(i+1,len(stock)) :
            if stock[j] - stock[i] > max_pfit :
                buy = stock[i]
                sell = stock[j]
                max_pfit = stock[j] - stock[i]
    print(buy,sell)

max_profit_double_for(stock)

