def myAtoi(s:str):
  index = 0
  result = 0
  sign = 1
  n = len(s)
  
  while index < n and s[index] == " ":
    index += 1
    
  if index < n and s[index] == "-":
    sign = -1
    index += 1
  elif index < n and s[index] == "+":
    index += 1
  
  while index < n and s[index].isdigit():
    result = result * 10 + int(s[index])
    index += 1
    
  result *= sign
  
  lower = -(2 ** 31)
  upper = 2**31 - 1
  
  return max(lower, min(result, upper))