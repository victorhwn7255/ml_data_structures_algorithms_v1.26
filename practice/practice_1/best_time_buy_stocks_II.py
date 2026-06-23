def maxProfit(prices: list[int]):
  results = 0
  
  for i in range(1, len(prices)):
    profits = prices[i] - prices[i-1]
    if profits > 0:
      results += profits
  
  return results


print(maxProfit([7,1,5,3,6,4]))