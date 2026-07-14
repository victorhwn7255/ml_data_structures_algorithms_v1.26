def isPalindrome(s: str):
  clean_str = ''.join(char.lower() for char in s if char.isalnum())
  
  left = 0
  right = len(clean_str) - 1
  
  while left <=right:
    if clean_str[left] != clean_str[right]:
      return False
    left += 1
    right -= 1
  
  return True



print(isPalindrome("A man, a plan, a canal: Panama"))


