def isHappy(n: int):
  seen = set()
  
  while n != 1:
    if n not in seen:
      seen.add(n)
    else:
      return False
    
    total = 0
    while n > 0:
      digit = n % 10
      total += digit ** 2
      n //= 10
  
    n = total
  
  return True