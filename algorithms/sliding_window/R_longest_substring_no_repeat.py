def lengthOfLongestSubstring(s: str):
  left = 0
  hash_map = {}
  result = 0
  
  for right in range(len(s)):
    if s[right] in hash_map and hash_map[s[right]] >= left:
      left = hash_map[s[right]] + 1
    
    hash_map[s[right]] = right
    result = max(result, right - left + 1) 

  return result

print(lengthOfLongestSubstring("abcabcbb"))