def myPow(x: float, n: int):
  if n == 0:
    return 1
  if x == 0:
    return 0
  
  result = 1
  
  if n < 0:
    x = 1/x
    n = -n
  
  while n > 0:
    if n % 2 == 1:
      result *= x
      
    x *= x
    n //= 2
  
  return result

