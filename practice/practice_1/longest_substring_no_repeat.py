def lengthOfLongestSubstring(s: str):
  hash_map = {}
  result = 0
  left = 0
  
  for right in range(len(s)):
    current_char = s[right]
    if current_char in hash_map and hash_map[current_char] >= left:
      left = hash_map[current_char] + 1
    hash_map[current_char] = right
    result = max(result, right - left + 1)
    
  return result

print(lengthOfLongestSubstring("abcabcbb"))

