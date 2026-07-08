def mySqrt(x: int):
  left = 0
  right = x
  result = 0
  
  while left <= right:
    mid = (left + right) // 2
    if mid * mid <= x:
      left = mid + 1
      result = mid
    else:
      right = mid - 1

  return result