def firstUniqChar(s: str):
  hash_map = {}
  
  for i, char in enumerate(s):
    if char not in hash_map:
      hash_map[char] = i
    else:
      hash_map[char] = float('inf')
  
  result = min(hash_map.values())
  
  return -1 if result == float('inf') else result