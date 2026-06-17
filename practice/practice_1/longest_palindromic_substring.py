def longestPalindrome(s: str):
  result = s[0]
  
  def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return s[left+1:right]
  
  for i in range(len(s)):
    odd_center = expand(i, i)
    even_center = expand(i, i+1)
    if len(odd_center) > len(result):
      result = odd_center
    if len(even_center) > len(result):
      result = even_center
      
  return result