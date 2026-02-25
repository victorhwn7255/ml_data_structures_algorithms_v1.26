def climbStairs(n):
  if n <= 2:
    return n
  
  two_back = 1
  one_back = 2
  
  for i in range(3, n+1):
    current = one_back + two_back
    two_back = one_back
    one_back = current

  return one_back

print(climbStairs(2))
print(climbStairs(3))