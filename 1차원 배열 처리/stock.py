def stock(prices):
    answer = []
    while prices:
        m = min(prices)
        num = prices.pop(0)
        if num == m:
            answer.append(len(prices))
        else:
            for i, p in enumerate(prices, 1):
                if num > p:
                    answer.append(i)
                    break

    return answer

prices = [3, 4, 5, 2, 1, 3]
print(stock(prices))
