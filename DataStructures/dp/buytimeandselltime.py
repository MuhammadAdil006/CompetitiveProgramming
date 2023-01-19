def stock(prices):
    i = 0
    valley = prices[0]
    peak = prices[0]
    profit = 0
    n = len(prices)
    while (i < len(prices)-1):
        while i < n-1 and (prices[i] >= prices[i+1]):
            i += 1
        valley = prices[i]
        peak = prices[i]
        while i < n-1 and prices[i+1] >= prices[i]:
            i += 1
        peak = prices[i]
        profit += peak-valley
        i += 1
    return profit


print(stock([7, 1, 5, 3, 6, 4]))
