def trailingZeroes(n: int):
  count = 0
  
  while n >= 5:
    n = n // 5
    count = count + n
  
  return count