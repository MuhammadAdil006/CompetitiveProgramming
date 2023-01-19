def stock(prices):
    # ans = 0
    # for i in range(len(prices)):
    #     buy = prices[i]
    #     if(len(prices[i+1:])!=0):
    #         sell = max(prices[i+1:])

    #         ans = max(ans, sell-buy)
    # return ans
    ans = 0
    mem = {}
    mem[0] = prices[0]
    for i in range(1, len(prices)):
        sell = prices[i]
        mem[i] = prices[i]
        mem[i] = min(mem[i], mem[i-1])
        buy = mem[i]
        ans = max(ans, sell-buy)
    return ans


print(stock([7, 1, 5, 3, 6, 4]))
