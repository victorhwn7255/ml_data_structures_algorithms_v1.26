def maxProfit(k: int, prices: list[int]):
    n = len(prices)
    if n == 0:
        return 0

    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    buy = [float('-inf')] * k
    sell = [0] * k

    for price in prices:
        buy[0] = max(buy[0], -price)
        sell[0] = max(sell[0], buy[0] + price)

        for i in range(1, k):
            buy[i] = max(buy[i], sell[i - 1] - price)
            sell[i] = max(sell[i], buy[i] + price)

    return sell[k - 1]


print(maxProfit(2, [2, 4, 1]))
print(maxProfit(2, [3,2,6,5,0,3]))