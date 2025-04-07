def maxProfit(prices):
    l, r = 0, 1
    maxP = 0
    buyday=sellday=0


    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            buyday=l
            sellday=r

            #print(l,r)
        else:
            l = r
        r += 1

    print(f"Buy in on {buyday} day  and sell it on {sellday}  day and max profit {maxP}")
    return maxP

print(maxProfit([7, 10, 1, 3, 6, 9, 2]))



#in second stock buy and seel u can sell and buy again and again
#put two pointer at i and i+1 and try to check if proce is i+1>i than sell it to get profir

def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])

    return profit

