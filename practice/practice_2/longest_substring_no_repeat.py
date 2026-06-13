def lengthOfLongestSubstring(s: str):
  hash_table = {}
  result = 0
  left = 0
  
  for right in range(len(s)):
    current_char = s[right]
    if current_char in hash_table and hash_table[current_char] >= left:
      left = hash_table[current_char] + 1

    hash_table[current_char] = right
    result = max(result, right-left+1)
  
  return result