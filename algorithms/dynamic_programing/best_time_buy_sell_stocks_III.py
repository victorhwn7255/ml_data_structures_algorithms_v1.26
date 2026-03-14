def maxProfit(prices: list[int]):
  buy_1 = float('-inf')
  sell_1 = 0
  buy_2 = float('-inf')
  sell_2 = 0
  
  for price in prices:
    buy_1 = max(buy_1, -price)
    sell_1 = max(sell_1, buy_1 + price)
    buy_2 = max(buy_2, sell_1-price)
    sell_2 = max(sell_2,buy_2+price)
  
  return sell_2

print(maxProfit([3,3,5,0,0,3,1,4]))