def titleToNumber(columnTitle: str):
  result = 0
  
  for i in range(len(columnTitle)-1, -1, -1):
    number = ord(columnTitle[i]) - ord('A') + 1
    power = len(columnTitle) -1 -i
    multiple = 26 ** power
    result += number * multiple
  
  return result


