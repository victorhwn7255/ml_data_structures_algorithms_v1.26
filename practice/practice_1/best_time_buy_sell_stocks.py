def maxProfit (prices: list[int]):
  lowest_price = prices[0]
  max_profits = 0
  
  for num in prices:
    lowest_price = min(num, lowest_price)
    max_profits = max(max_profits, num-lowest_price)
  
  return max_profits